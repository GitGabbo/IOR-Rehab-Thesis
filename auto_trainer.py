import numpy as np
import extracted_data_reader
from tsai.all import *
import time


def train(ex_number, batch_size=32, epochs_number=20, verbose=False):
    FRAME_NUMBERS = ["mean", "max", "min"]

    Y = extracted_data_reader.read_target_ex(ex_number=ex_number)
    y = np.array([y[:5] for y in Y])

    for frame_number in FRAME_NUMBERS:
        X = np.array(extracted_data_reader.read_data_ex(
            ex_number=ex_number, frame_number=frame_number))
        if verbose:
            print(
                f"Starting ex{ex_number} training process for {frame_number}")

        len_y = len(y)

        # leave-one-out cross validation
        splits = get_splits(y, n_splits=len(y), shuffle=False, show_plot=False)

        tfms = [None, TSClassification()]
        accuracies = []
        start = time.time()
        # leave-one-out cross validation
        for i, split in enumerate(splits):
            if verbose:
                print(f"Video {i}/{len_y}")
            # create the datasets
            ds = TSDatasets(X, y, splits=split, tfms=tfms, inplace=True)
            # create the data loader from the datasets
            dls = TSDataLoaders.from_dsets(
                ds.train, ds.valid, bs=batch_size, batch_tfms=tfms, num_workers=0)
            if show_images:
                dls.show_batch(sharey=True)
            # create learner of an InceptionTimePlus model
            learn = ts_learner(dls, 'InceptionTimePlus', metrics=accuracy)
            # fit the model
            if verbose:
                print(f"Start fit")
            learn.fit_one_cycle(epochs_number, 1e-3)
            if verbose:
                print(f"End fit")
            accuracies.append(learn.validate()[1])

        end = time.time() - start

        # get mean accuracies
        mean_acc = round(np.mean(np.array(accuracies)), 6)

        if verbose:
            print(f"\n\n")
            print(f"Mean accuracy: {mean_acc}\nTime: {end}")
        # log results
        with open("logs/ts_logs.md", "a") as f:
            f.write(f"EX{ex_number} {frame_number}\t\t{mean_acc}\t{end}\n")

        # save learner
        learn.export(f"models/ex{ex_number}_{frame_number}.pkl")
        if verbose:
            print(f"Saved model")

        print("Done.\n\n\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        for i in range(1, 6):
            train(i)
    else:
        train(sys.argv[1])
