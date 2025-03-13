import pandas as pd
import openpyxl
from datetime import datetime

def extract_times(file_path, col_names):
    time_df = pd.read_csv(file_path, names=col_names)

    return time_df

def transform_name(transform_df):
    transform_df["Full Name"] = transform_df["First Name"].values + " " + transform_df["Last Name"].values

    transform_df["Entry"] = transform_df["Date"].values + " " + transform_df["Time"].values

    fullname_df = transform_df.loc[:, ["id", "Full Name", "Biometrics", "Entry"]]

    fullname_df["Entry"] = pd.to_datetime(fullname_df["Entry"])

    return fullname_df

def load_to_excel(dataframe, file_path):
    dataframe.to_excel(file_path, engine="openpyxl", index=False)

if __name__ == "__main__":
    print("Not to be used on it's own, functions must be imported")
