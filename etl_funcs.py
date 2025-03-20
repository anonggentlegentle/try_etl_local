import pandas as pd
import openpyxl
from datetime import datetime
from tkinter.filedialog import askopenfilename, askdirectory
from excel_formatting import format_excel_file

def extract_times(file_path, col_names):
    time_df = pd.read_csv(file_path, names=col_names, skiprows=1)

    return time_df

def transform_name(transform_df):
    transform_df["Full Name"] = transform_df["First Name"].values + " " + transform_df["Last Name"].values

    # transform_df["Entry"] = transform_df["Date"].values + " " + transform_df["Time"].values

    transform_df["Entry"] = pd.to_datetime(transform_df["Date"] + " " + transform_df["Time"], format="mixed")

    fullname_df = transform_df.loc[:, ["id", "Full Name", "Biometrics", "Entry"]]

    # fullname_df["Entry"] = pd.to_datetime(fullname_df["Entry"], format="%d-%b-%Y %H:%M:%S")

    return fullname_df

def load_to_excel(dataframe, final_file_path):
    final_file = final_file_path.replace(".csv", "-NEW.xlsx")

    dataframe.to_excel(final_file, engine="openpyxl", index=False)

    format_excel_file(final_file)

if __name__ == "__main__":
    print("Not to be used on it's own, functions must be imported")
