import numpy as np
import extracted_data_reader
from tsai.all import *
import matplotlib.pyplot as plt
import time
import os

def train(ex_number, batch_size=[32, 64, 128], epochs_number=20, find_best_lr=False, verbose=True):
    FRAME_NUMBERS = ["mean", "max", "min"]

    Y = extracted_data_reader.read_target_ex(ex_number=ex_number)
    y = np.array([y[:5] for y in Y])

    for frame_number in FRAME_NUMBERS:
        image_base_name = f"C:/Users/Gabriele/Downloads/Uni/IOR-Rehab-Thesis/images/models/ex{ex_number}/ex{ex_number}_{frame_number}"

        X = np.array(extracted_data_reader.read_data_ex(ex_number=ex_number, frame_number=frame_number))
        if verbose: print(f"Starting ex{ex_number} training process for {frame_number}")

        # leave-one-out cross validation
        splits = get_splits(y, n_splits=len(y), shuffle=False, show_plot=False)
        if verbose: print(f"Created splits")
        # create datasets
        tfms = [None, TSClassification()]
        dsets = []
        for split in splits:
            dsets.append(TSDatasets(X, y, splits=split, tfms=tfms, inplace=True))
        if verbose: print(f"Created datasets")

        # load datasets
        dls   = TSDataLoaders.from_dsets(*dsets, bs=batch_size, batch_tfms=[TSStandardize()], num_workers=0)
        # dls.show_batch(sharey=True)
        if verbose: print(f"Created dataloaders")


        # create learner
        learn = ts_learner(dls, 'InceptionTimePlus', metrics=accuracy)
        if find_best_lr: 
            learn.lr_find()
            plt.savefig(f"{image_base_name}_lr.jpg")
            if verbose: print(f"Found best lr")

        if verbose: print(f"Start fit")
        start = time.time()
        learn.fit_one_cycle(epochs_number, lr_max=1e-3)
        end = time.time() - start
        print(f"EX{ex_number}\t{frame_number}")
        if verbose: print(f"End fit\nTime elapsed: {end} s")

        # save learner
        learn.export(f"models/ex{ex_number}_{frame_number}.pkl")
        if verbose: print(f"Saved model")

        learn.recorder.plot_metrics(figname=f"{image_base_name}_metrics.png")
        learn.show_results(figname=f"{image_base_name}_results.png")
        # learn.show_probas(figname=f"{image_base_name}_probas.png")
        interp = ClassificationInterpretation.from_learner(learn)
        interp.plot_confusion_matrix(figname=f"{image_base_name}_confusion_matrix.png")

        print("Done.\n\n\n")



if __name__ == "__main__":
    if len(sys.argv) < 2:
        for i in range(1,6):
            train(i)
    else: train(sys.argv[1])