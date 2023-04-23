# IOR-Rehab-Thesis
## Introduction
Master Thesis in Computer Science @ Alma Mater Studiorum in collaboration with [Istituto Ortopedico Rizzoli](https://www.ior.it/).

The aim of the project is to develop a multimodal neural network able to automatically predict 5 scores regarding the rehabilitation of patients. Doctors from IOR:
* Recorded patients doing 5 different types of exercises in 2 sessions, each of which with more or less 10 repetitions: the first session was recorded before phisical rehabilitation, the second one after it; 
* Marked 5 scores for each repetition of each session: Goal, Width of movement, Head position, Shoulders position, Trunk position. Each score ranges from 1 to 5, where 5 is the highest;
* Stored data of patients (sex, age, ...)

## 1. Data preparation
### 1.1. Video extractor
I used mediapipe python library inside `video_data_extractor.py` to extract the coordinates of 9 joints for each frame of every video. Then I exported the keypoints in `.csv` format inside `videos_data`. The joints are: nose (head), shoulder (left and right), elbow (left and right), wrist (left and right) and waist (left and right).

### 1.2. Target extraction
The next step is to extract the targets from `scores.xlsx`, the file created by the doctors from IOR which contains the 5 marked scores for each repetition, session and patient, using `target_data_extractor.py`.

## 2. Model training


## Libraries used
* [Numpy](https://numpy.org/)
* [Opencv-python](https://pypi.org/project/opencv-python/)
* [Pandas](https://pandas.pydata.org/)
* [Matplotlib](https://matplotlib.org/stable/index.html)
* [Mediapipe](https://pypi.org/project/mediapipe/)