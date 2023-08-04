import os
import time
import numpy as np
from tsai.all import *
from fastai.tabular.core import *
import extracted_data_reader


def train(ex_number, epochs_number=20, verbose=True):
    FRAME_NUMBERS = ["mean", "max", "min"]
    TARGETS_NAME = ["goal", "width", "head", "shoulders", "trunk"]

    # get demographic data
    df = []
    df_dir = f"final_tab_data/ex{ex_number}/"
    for file in sorted(os.listdir(df_dir)):
        df.append(pd.read_csv(os.path.join(df_dir, file)))
    df = pd.concat(df, axis=0, ignore_index=True)

    Y = extracted_data_reader.read_target_ex(ex_number=ex_number)
    for i, target in enumerate(TARGETS_NAME):
        y = np.array([y[i] for y in Y])

        for frame_number in FRAME_NUMBERS:
            # image_base_name = f"C:/Users/Gabriele/Downloads/Uni/IOR-Rehab-Thesis/images/multi-models/ex{ex_number}/ex{ex_number}_{frame_number}_{target}"

            X = np.array(extracted_data_reader.read_data_ex(
                ex_number=ex_number, frame_number=frame_number))
            print(
                f"Starting training process for ex{ex_number} {frame_number} {target}")

            # get features from timeseries data
            ts_features = get_ts_features(X, y)
            if verbose:
                print("Extracted features")

            # merge timeseries data with demographic data
            ts_features.insert(loc=0, column='age', value=df['age'])
            ts_features.insert(loc=0, column='height', value=df['height'])
            ts_features.insert(loc=0, column='weight', value=df['weight'])
            ts_features.insert(loc=0, column='bmi', value=df['bmi'])
            ts_features.insert(loc=0, column='gender', value=df['gender'])

            # data to build data loaders
            splits = get_splits(ts_features, n_splits=len(
                ts_features), shuffle=False, show_plot=False)
            procs = [Categorify, FillMissing, Normalize]
            cat_names = ['gender']
            cont_names = list(ts_features.columns)[1:-1]
            y_names = 'target'
            y_block = CategoryBlock()

            accuracies = []

            if verbose:
                print(f"Start fit")
            start = time.time()
            # leave-one-out cross validation
            for split in splits:
                # create dataloader
                to = TabularPandas(ts_features, cat_names=cat_names, cont_names=cont_names,
                                   y_names=y_names, splits=split, procs=procs, y_block=y_block, inplace=True)
                tab_dls = to.dataloaders(bs=32)
                # create model
                tab_model = build_tabular_model(TabModel, dls=tab_dls)
                # create learner
                learnTab = Learner(tab_dls, tab_model, metrics=accuracy)
                # fit learner
                learnTab.fit_one_cycle(epochs_number, 1e-3)
                # append accuracy
                accuracies.append(learnTab.validate()[1])

            end = time.time() - start
            # get mean accuracies
            mean_acc = round(np.mean(np.array(accuracies)), 6)

            if verbose:
                print(f"\n\n")
                print(f"Mean accuracy: {mean_acc}\nTime: {end}")

            # log results
            with open("logs/multi_logs.md", "a") as f:
                f.write(
                    f"EX{ex_number} {target} {frame_number}\t\t{mean_acc}\t{end}\n")

            # save the model
            learnTab.export(
                f"multi-models/ex{ex_number}/ex{ex_number}_{frame_number}_{target}.pkl")

            if verbose:
                print(f"Saved model")
            print("Done.\n\n\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        for i in range(1, 6):
            train(i)
    else:
        train(int(sys.argv[1]))
