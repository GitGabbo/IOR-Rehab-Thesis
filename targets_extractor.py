import os
import pandas as pd
import sys

def extract_targets(ex_number):
    my_sheets = pd.ExcelFile('../1- Old/Intelligenza Artificiale/Progetto/ai_leoniturchesivanigliati/scores.xlsx')
    NAMES = my_sheets.sheet_names

    ROWS = [
        # Rows Ex 1
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        # Rows Ex 2
        [14, 15, 16, 17, 17, 18, 20, 21, 22, 23, 24],
        # Rows Ex 3
        [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38],
        # Rows Ex 4
        [41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51],
        # Rows Ex 5
        [55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]
    ]

    # for each sheet of the excel file
    for i in range(1, 20):
        book = pd.read_excel("../1- Old/Intelligenza Artificiale/Progetto/ai_leoniturchesivanigliati/scores.xlsx", engine='openpyxl', sheet_name=i)
        COLS_SES1 = [1, 2, 3, 4, 5, 6]
        COLS_SES2 = [12, 13, 14, 15, 16, 17]
        ROWS_EX = ROWS[ex_number - 1]
        # data frame
        df = pd.DataFrame(book)
        df = df.rename(columns={'1= Per nulla': 'Goal', '2= Poco': 'Width', '3= Abbastanza': 'Head', '4= Molto': 'Shoulders', '5= Moltissimo': 'Trunk', 'Unnamed: 6': 'Score', '1= Per nulla.1': 'Goal', '2= Poco.1': 'Width', '3= Abbastanza.1': 'Head', '4= Molto.1': 'Shoulders', '5= Moltissimo.1': 'Trunk', 'Unnamed: 17': 'Score' })

        ses_1 = df.iloc[ROWS_EX, COLS_SES1].dropna()
        ses_2 = df.iloc[ROWS_EX, COLS_SES2].dropna() 

        if not NAMES[i][3].isspace():
            NAMES[i] = NAMES[i][:3] + " " + NAMES[i][3:]

        if(len(ses_1.index) > 2): 
            ses_1.to_csv(f'targets_data/ex{ex_number}/{NAMES[i]} {ex_number}.1.csv', index = False, header=True)
        

        if(len(ses_2.index) > 2): 
            ses_2.to_csv(f'targets_data/ex{ex_number}/{NAMES[i]} {ex_number}.2.csv', index = False, header=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        for i in range(1,6):
            extract_targets(i)
    else: extract_targets(sys.argv[1])