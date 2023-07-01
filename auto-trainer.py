import numpy as np
import extracted_data_reader
from tsai.all import *
import matplotlib.pyplot as plt
import time
import os

def train(ex_number, batch_size=[32, 64, 128], epochs_number=20, find_best_lr=False, verbose=True):
    TARGETS_LABELS = ["goal","width","head","shoulders","trunk"]
    FRAME_NUMBERS = ["mean", "max", "min"]

    Y = extracted_data_reader.read_target_ex(ex_number=ex_number)
    for i,target_name in enumerate(TARGETS_LABELS):
        y = [y[i] for y in Y]
        for frame_number in FRAME_NUMBERS:
            image_base_name = f"C:/Users/Gabriele/Downloads/Uni/IOR-Rehab-Thesis/images/models/ex{ex_number}/ex{ex_number}_{frame_number}_{target_name}"

            X = np.array(extracted_data_reader.read_data_ex(ex_number=ex_number, frame_number=frame_number))
            if verbose: print(f"Starting ex{ex_number} training process for {frame_number} {target_name}")

            # leave-one-out cross validation
            splits = get_splits(y, n_splits=len(y), shuffle=False, show_plot=False)
            if verbose: print(f"Created splits")
            # create datasets
            tfms  = [None, [Categorize()]]
            dsets = []
            for split in splits:
                dsets.append(TSDatasets(X, y, splits=split, tfms=tfms, inplace=True))
            if verbose: print(f"Created datasets")

            # load datasets
            dls   = TSDataLoaders.from_dsets(*dsets, bs=batch_size, batch_tfms=[TSStandardize()], num_workers=0)
            # dls.show_batch(sharey=True)
            if verbose: print(f"Created dataloaders")


            # create model
            model = InceptionTime(dls.vars, dls.c)

            # create learner
            learn = Learner(dls, model, metrics=accuracy)
            if find_best_lr: 
                learn.lr_find()
                plt.savefig(f"{image_base_name}_lr.jpg")
                if verbose: print(f"Found best lr")

            if verbose: print(f"Start fit")
            learn.fit_one_cycle(epochs_number, lr_max=1e-3)
            print(f"EX{ex_number}\t{frame_number}\t{target_name}")
            if verbose: print(f"End fit")

            # save learner
            learn.save_all(path=f'models_export/ex{ex_number}/', dls_fname=f'dls/{frame_number}_ex{ex_number}_{target_name}_dls', 
                   model_fname=f'{frame_number}_ex{ex_number}_{target_name}', learner_fname=f'{frame_number}_ex{ex_number}_{target_name}_learner')
            if verbose: print(f"Saved model")

            print(image_base_name)
            learn.recorder.plot_metrics(figname=f"{image_base_name}_metrics.png")
            learn.show_results(figname=f"{image_base_name}_results.png")
            learn.show_probas(figname=f"{image_base_name}_probas.png")
            interp = ClassificationInterpretation.from_learner(learn)
            interp.plot_confusion_matrix(figname=f"{image_base_name}_confusion_matrix.png")

            dls_dir = f"models_export/ex{ex_number}/dls"
            for file in os.listdir(f"models_export/ex{ex_number}/dls"):
                os.remove(f"{dls_dir}/{file}")

            print("Done.\n\n\n")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        for i in range(1,6):
            train(i)
    else: train(sys.argv[1])