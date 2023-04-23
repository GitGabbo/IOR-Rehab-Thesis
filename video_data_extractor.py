import cv2
import mediapipe as mp
import time
import os
import sys
import numpy as np
import matplotlib.pyplot as plt

# mediapipe joints numbers
# 0: nose, 11: shoulder l, 12: shoulder r, 13: elbow l, 14: elbow r 
# 15: wrist l, 16: wrist r, 23: waist l, 24: waist r
JOINTS = [0, 11, 12, 13, 14, 15, 16, 23, 24]

# each position is for each joint, one for X and one for Y
joints_positions = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

# add joints position in the new frame
def add_points(results, img, view_videos_flag):
    global joints_positions
    global JOINTS

    if results.pose_landmarks:
        for i, lm in enumerate(results.pose_landmarks.landmark):
            # if joint is to draw
            if i in JOINTS:
                # draw circe in the right spot if user views the video
                if view_videos_flag:
                    h, w, _ = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(img, (cx, cy), 5, (0, 255, 0), cv2.FILLED)

                # get the index of the joint
                joint_index = JOINTS.index(i)

                # append the keypoint in joints_positions
                joints_positions[joint_index*2].append(lm.x)
                # saving (1-y) so that (0,0) is at bottom-left and not upper-left 
                joints_positions[joint_index*2+1].append(1 - lm.y)

# export data in csv format
def export_data(file_name, ex_number):
    global joints_positions

    file_name = file_name.replace(".mp4", ".csv")
    output_file = f'videos_data/ex{ex_number}/{file_name}'

    # open output file
    with open(output_file, "w") as f:

        # write header: features names
        f.write("HeadX,HeadY,ShoulderLX,ShoulderLY,ShoulderRX,ShoulderRY,ElbowLX,ElbowLY,ElbowRX,ElbowRY,WristLX,WristLY,WristRX,WristRY,WaistLX,WaistLY,WaistRX,WaistRY\n")

        number_of_frames = len(joints_positions[0])
        number_of_joints = len(joints_positions)
        # for each frame
        for frame in range(number_of_frames):
            # for each joint
            for i, joint in enumerate(joints_positions):
                    # if it's the last joint of the last frame
                    if i ==  number_of_joints - 1 and frame == number_of_frames - 1:
                        # print without new line nor comma
                        f.write(f"{str(joint[frame])}")
                    # if it's the last joint
                    elif i ==  number_of_joints - 1:
                        # print new line
                        f.write(f"{str(joint[frame])}\n")
                    else:
                        # else print comma
                        f.write(f"{str(joint[frame])},")

# extract data from one exercise
def extract_data_ex(ex_number, view_videos_flag):
    global joints_positions
    global JOINTS

    # initialize mediapipe
    mpPose = mp.solutions.pose
    pose = mpPose.Pose()

    # videos directory
    directory = f"videos/es{ex_number}/"

    # for each video
    for file in os.listdir(directory):
        joints_positions = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        # get file
        f = os.path.join(directory, file)
        # start cv video capture
        cap = cv2.VideoCapture(f"{f}")
        cap.set(cv2.CAP_PROP_FPS, 5) 
        pTime = 0
        # for each frame
        while True:
            # get the image
            success, img = cap.read()

            # check if video is ended
            if not success:
                print(f"Can't receive frame. Done {file}")
                break

            # color image
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # process the image with mediapipe
            results = pose.process(imgRGB)

            # draw points on image and save them
            add_points(results, img, view_videos_flag)

            if view_videos_flag:
                # write fps on image
                cTime = time.time()
                fps = 1 /(cTime - pTime)
                pTime = cTime
                cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

                # show image and wait 1ms
                cv2.imshow(f"{f}", img)
                cv2.waitKey(1)

        export_data(file, ex_number)

        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":

    view_videos_flag = False
    
    # check if the excercise number is present 
    if len(sys.argv) == 2:
        # get exercise number
        ex_number = int(sys.argv[1])
        extract_data_ex(ex_number=ex_number, view_videos_flag=view_videos_flag)
    else :
        for i in range(1,6):
           extract_data_ex(ex_number=i, view_videos_flag=view_videos_flag) 