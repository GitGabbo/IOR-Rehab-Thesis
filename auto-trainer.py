import numpy as np
import extracted_data_reader
from tsai.all import *

def train(ex_number, frame_number, batch_size=32, epochs_number=15, find_best_lr=False):
    X = np.array(extracted_data_reader.read_data_ex(ex_number=ex_number, frame_number=frame_number))
    Y = extracted_data_reader.read_target_ex(ex_number=ex_number)
    TARGETS_LABELS = ["Goal","Width","Head","Shoulders","Trunk"]

    for i,target_name in enumerate(TARGETS_LABELS):
        y = [y[i] for y in Y]
        # leave-one-out cross validation
        splits = get_splits(y, n_splits=len(y), shuffle=False, show_plot=False)
        
        # create datasets
        tfms  = [None, [Categorize()]]
        dsets = []
        for split in splits:
            dsets.append(TSDatasets(X, y, splits=split, tfms=tfms, inplace=True))

        # load datasets
        dls   = TSDataLoaders.from_dsets(*dsets, bs=batch_size, batch_tfms=[TSStandardize()], num_workers=0)
        if show_images: dls.show_batch(sharey=True)

        # create model
        model = InceptionTime(dls.vars, dls.c)

        # create learner
        learn = Learner(dls, model, metrics=accuracy)
        if find_best_lr: learn.lr_find()
        learn.fit_one_cycle(epochs_number, lr_max=1e-3)
        if show_images: learn.plot_metrics()

        # save learner
        stage_name = f"ex{ex_number}_stage0_{target_name}"
        learn.save(stage_name)
        if show_images:
            learn.show_probas()
            interp = ClassificationInterpretation.from_learner(learn)
            interp.plot_confusion_matrix()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        for i in range(1,6):
            train(i, "mean")
    if len(sys.argv) < 3:
        train(sys.argv[1], "mean")
    else: train(sys.argv[1], sys.argv[2])