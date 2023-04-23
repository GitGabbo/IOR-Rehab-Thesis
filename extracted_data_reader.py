import os
import numpy as np
import matplotlib.pyplot as plt
import sys

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
    
def read_data_ex(ex_number):
    # csv directory
    directory = f"videos_data/ex{ex_number}/"
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

    visualize_improvement("002 DL", 1, 1)

    return data

if __name__ == "__main__":

    # check if the excercise number is present 
    if len(sys.argv) == 2:
        # get exercise number
        ex_number = int(sys.argv[1])
        read_data_ex(ex_number=ex_number)
    else :
        for i in range(1,6):
           read_data_ex(ex_number=i) 
