import os
import sys
import extracted_data_reader
import pandas as pd
import numpy as np
import shutil

def finalize_exercise(ex_number):
    VIDEO_CSV_DIR = f"videos_data/ex{ex_number}/"
    TARGET_CSV_DIR = f"targets_data/ex{ex_number}/"
    FINAL_VIDEO_DIR = f"final_video_data/ex{ex_number}/"
    FINAL_TARGETS_DIR = f"final_targets_data/ex{ex_number}/"

    TARGET_CSV_FILES = os.listdir(TARGET_CSV_DIR)

    # for each valutation file
    for file in TARGET_CSV_FILES:
        # take the first 6 characters of the name of files in VIDEO_CSV_DIR (ad es. "001 SJ")
        name_initial = file[:6]

        with open(TARGET_CSV_DIR+file, "r") as score_f:
            targets_lines = score_f.readlines()[1:-1]
            number_reps = len(targets_lines)

            for rep in range(number_reps):
                # video name (e.g. "001 SJ" + "1.1" + ".1" + ".csv")
                video_name_file = f"{name_initial}.{file[10:13]}.{rep+1}.csv"
                # open video file and merged file
                try:
                    shutil.copy2(f"{VIDEO_CSV_DIR}{video_name_file}", f"{FINAL_VIDEO_DIR}{video_name_file}")
                except FileNotFoundError:
                    print(f"Video file {video_name_file} does not exist, skipping its valutation file")
                    TARGET_CSV_FILES.remove(file)
                except ZeroDivisionError:
                    print(f"Video file {video_name_file} could not be analyzed by mediapipe. Skipping repetition and its valutation")
                    TARGET_CSV_FILES.remove(file)

    for file in TARGET_CSV_FILES:
        shutil.copy2(f"{TARGET_CSV_DIR}{file}", f"{FINAL_TARGETS_DIR}{file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        for i in range(1,6):
            finalize_exercise(i)
    else: finalize_exercise(sys.argv[1])