import pandas as pd
import os
import sys

def merge(ex_number=1):
    target_dir = f"final_targets_data/ex{ex_number}/"
    demo_info_df = pd.read_csv("demographic_data/demographic_info.csv")
    i = 0
    for j,file in enumerate(sorted(os.listdir(target_dir))):
        i = int(j/2)
    # for j,file in enumerate(sorted(os.listdir(target_dir))[23:]):
    #     i = int(j/2) + 12
        file_df = pd.read_csv(os.path.join(target_dir, file))
        reps_number = file_df.shape[0]
        id_name = f"{demo_info_df.iloc[i,0][:3]} {demo_info_df.iloc[i,0][3:]}"
        id_col = [id_name] * reps_number
        age_col = [f"{demo_info_df.iloc[i,1]}"] * reps_number
        height_col = [f"{demo_info_df.iloc[i,2]}"] * reps_number
        weight_col = [f"{demo_info_df.iloc[i,3]}"] * reps_number
        bmi_col = [f"{demo_info_df.iloc[i,4]}"] * reps_number
        gender_col = [f"{demo_info_df.iloc[i,5]}"] * reps_number
        file_df['id'] = id_col
        file_df['age'] = age_col
        file_df['height'] = height_col
        file_df['weight'] = weight_col
        file_df['bmi'] = bmi_col
        file_df['gender'] = gender_col
        file_df = file_df.iloc[:-1]

        file_df.to_csv(f"final_tab_data/ex{ex_number}/{file}", index=False)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        for i in range(1,6):
            merge(i)
    else: merge(sys.argv[1])