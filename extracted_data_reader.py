import os
import numpy as np
import matplotlib.pyplot as plt
import sys
import math

LABELS = ['HeadX', 'HeadY', 'ShoulderLX', 'ShoulderLY', 'ShoulderRX', 'ShoulderRY', 'ElbowLX', 
            'ElbowLY', 'ElbowRX', 'ElbowRY', 'WristLX', 'WristLY', 'WristRX', 'WristRY', 'WaistLX', 
            'WaistLY', 'WaistRX', 'WaistRY']

# visualize video data
def visualize_video_data(data, video_name):
    global LABELS

    figure, axis = plt.subplots(1,2)
    # get the number of frames
    x_vals = np.arange(len(data[0]))

    # for each joint
    for j, joint in enumerate(data):
        # visualize only Y coordinates
        if j % 2 != 0:
            axis[1].plot(x_vals, joint, label=LABELS[j])
        # visualize only X coordinates
        elif j % 2 == 0:
            axis[0].plot(x_vals, joint, label=LABELS[j])

    axis[0].set_xlabel("Frame")
    axis[1].set_xlabel("Frame")
    axis[0].set_ylabel("Screen value")
    axis[1].set_ylabel("Screen value")
    axis[0].set_title(f"{video_name} - X values")
    axis[1].set_title(f"{video_name} - Y values")
    figure.legend(loc="upper right")
    plt.show()

# visualize improvement of one person across the two sessions
def visualize_improvement(person_initials, ex_number, rep_number):
    global LABELS

    # csv files
    file_first_session = f"videos_data/ex{ex_number}/{person_initials}.{ex_number}.1.{rep_number}.csv"
    file_second_session = f"videos_data/ex{ex_number}/{person_initials}.{ex_number}.2.{rep_number}.csv"
    data = []
    # for each video
    for file in [file_first_session, file_second_session]:
        file_data = []
        # open video
        with open(file, 'r') as f:
            # skip header line
            file_lines = f.readlines()[1:]
            # for each line create a list of float numbers 
            file_data = [ [ float(y) for y in x.split(",") ] for x in file_lines  ]
        # save data in transposed form
        video_data = np.array(file_data).T
        # append video data
        data.append(video_data)

    _, axis = plt.subplots(2,2)

    for i, video in enumerate(data):
        # get the number of frames
        x_vals = np.arange(len(video[0]))
        # for each joint
        for j, joint in enumerate(video):
            # visualize only Y coordinates
            if j % 2 != 0:
                axis[i, 1].plot(x_vals, joint, label=LABELS[j])
            # visualize only X coordinates
            elif j % 2 == 0:
                axis[i, 0].plot(x_vals, joint, label=LABELS[j])
        axis[i, 0].set_title(f"{person_initials}.{ex_number}.{i+1}.{rep_number} - X Values")
        axis[i, 1].set_title(f"{person_initials}.{ex_number}.{i+1}.{rep_number} - Y Values")
        axis[i, 0].legend(bbox_to_anchor=(1.1, 0.5), loc="center")
        axis[i, 1].legend(bbox_to_anchor=(1.1, 0.5), loc="center")
        

    axis[1, 0].set_xlabel("Frame")
    axis[1, 1].set_xlabel("Frame")
    axis[0, 0].set_ylabel("Screen value")
    axis[1, 0].set_ylabel("Screen value")
    plt.subplots_adjust(left=0.062, wspace=0.37, hspace=0.305)
    plt.show()

def visualize_adjustment(video_data, mean_data, max_data, min_data, video_index=0):
    global LABELS
    
    _, axis = plt.subplots(4,2)

    videos = [video_data, mean_data, max_data, min_data]
    names = ["Input video", "Mean data", "Max data", "Min data"]

    for i, video in enumerate(videos):
        video = video[video_index]
        # get the number of frames
        x_vals = np.arange(len(video[0]))
        frame_number = len(video[0])
        # for each joint
        for j, joint in enumerate(video):
            # visualize only Y coordinates
            if j % 2 != 0:
                axis[i, 1].plot(x_vals, joint, label=LABELS[j])
            # visualize only X coordinates
            elif j % 2 == 0:
                axis[i, 0].plot(x_vals, joint, label=LABELS[j])
        axis[i, 0].set_title(f"{names[i]} with {frame_number} frames - X Values")
        axis[i, 1].set_title(f"{names[i]} with {frame_number} frames - Y Values")
        
        
    axis[1, 0].legend(bbox_to_anchor=(1.145, -0.42), loc="center")
    axis[1, 1].legend(bbox_to_anchor=(1.145, -0.42), loc="center")
    axis[3, 0].set_xlabel("Frame")
    axis[3, 1].set_xlabel("Frame")
    axis[0, 0].set_ylabel("Screen value")
    axis[1, 0].set_ylabel("Screen value")
    axis[2, 0].set_ylabel("Screen value")
    axis[3, 0].set_ylabel("Screen value")
    plt.subplots_adjust(left=0.062, wspace=0.37, hspace=0.8)
    plt.show()

def increase_frame_number(video_data, frame_number):
    ratio = len(video_data[0]) / frame_number
    adjusted_video_data = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] 
    
    prev_i = 0
    i = 0
    # foreach frame
    while (i < frame_number and i < len(video_data[0])):
        # foreach feature
        for j in range(len(video_data)):
            adjusted_video_data[j].append(video_data[j][i])
        # skip ceil(i+ratio) frames
        i = prev_i + ratio
        prev_i = i
        i = math.floor(i)

    i = math.floor(i - ratio) + 1
    if (len(adjusted_video_data[0]) < frame_number):
        for j in range(len(video_data)):
            adjusted_video_data[j].append(video_data[j][i])
    elif (len(adjusted_video_data[0]) > frame_number):
        for j in range(len(video_data)):
            adjusted_video_data[j].pop()

    return adjusted_video_data

def decrease_frame_number(video_data, frame_number):
    ratio = len(video_data[0])/frame_number
    adjusted_video_data = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []] 
    
    prev_i = 0
    i = 0
    # foreach frame
    while (i < len(video_data[0])):
        # foreach feature
        for j in range(len(video_data)):
            # append body data
            adjusted_video_data[j].append(video_data[j][i])
        # skip ceil(i+ratio) frames
        i = prev_i + ratio
        prev_i = i
        i = math.ceil(i)
    
    # check if there is still some frames missing
    if (len(adjusted_video_data[0]) < frame_number):
        i = math.floor(i - ratio) + 1
        for j in range(len(video_data)):
            adjusted_video_data[j].append(video_data[j][i])
    elif (len(adjusted_video_data[0]) > frame_number):
        for j in range(len(video_data)):
            adjusted_video_data[j].pop()

    return adjusted_video_data

def adjust_videos_frame_number(data, frame_number):
    adjusted_data = []
    for video in data:
        if(len(video[0]) > frame_number):
            adjusted_data.append(decrease_frame_number(video, frame_number))
        elif(len(video[0]) < frame_number):
            adjusted_data.append(increase_frame_number(video, frame_number))
        else:
            adjusted_data.append(video)

    print(len(adjusted_data))
    return adjusted_data

def read_data_ex(ex_number, frame_number=""):
    # csv directory
    directory = f"final_video_data/ex{ex_number}/"
    data = []
    # for each video
    for file in os.listdir(directory):
        file_data = []
        # open video
        with open(os.path.join(directory, file), 'r') as f:
            # skip header line
            file_lines = f.readlines()[1:]
            # for each line create a list of float numbers 
            file_data = [ [ float(y) for y in x.split(",") ] for x in file_lines  ]
        # save data in transposed form
        video_data = np.array(file_data).T
        # append video data
        data.append(video_data)

    if frame_number == "mean":
        # mean
        lengths = np.array([])
        for video in data:
            lengths = np.append(lengths, len(video[0]))
        mean = int(np.mean(lengths))
        return adjust_videos_frame_number(data, mean)
    elif frame_number == "max":
        # max
        lengths = np.array([])
        for video in data:
            lengths = np.append(lengths, len(video[0]))
        max = int(np.max(lengths))
        return adjust_videos_frame_number(data, max)
    elif frame_number == "min":
        # min
        lengths = np.array([])
        for video in data:
            lengths = np.append(lengths, len(video[0]))
        min = int(np.min(lengths))
        return adjust_videos_frame_number(data, min)
    elif frame_number == "":
        return data
    else:
        frame_number = int(frame_number)
        return adjust_videos_frame_number(data, frame_number)

def read_target_ex(ex_number):
    # csv directory
    directory = f"final_targets_data/ex{ex_number}/"
    data = []
    # for each video
    for file in os.listdir(directory):
        # open video
        with open(os.path.join(directory, file), 'r') as f:
            # skip header line
            file_lines = f.readlines()[1:-1]
            # for each line create a list of float numbers 
            for x in file_lines:
                data.append([ int(y) for y in x.split(",") ])
    print(len(data))
    return data

if __name__ == "__main__":

    # check if the excercise number is present 
    if len(sys.argv) == 2:
        # get exercise number
        ex_number = int(sys.argv[1])
        visualize_adjustment(read_data_ex(ex_number=ex_number), read_data_ex(ex_number=ex_number, frame_number="mean"), read_data_ex(ex_number=ex_number, frame_number="max"), read_data_ex(ex_number=ex_number, frame_number="min"), 77)
        read_data_ex(ex_number=ex_number, frame_number="mean")
        read_target_ex(ex_number)
    else :
        for i in range(1,6):
           read_data_ex(ex_number=i) 
