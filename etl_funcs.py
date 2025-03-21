import pandas as pd
from excel_formatting import format_excel_file
import datetime as dt

# Extracting the data from csv file into a dataframe
def extract_times(file_path, col_names):
    time_df = pd.read_csv(file_path, names=col_names, skiprows=0)

    return time_df

# Transforming the extracted dataframe
def transform_name(transform_df):
    # Create Full Name column from the First Name and Last Name columns
    transform_df["Full Name"] = transform_df["First Name"].values + " " + transform_df["Last Name"].values

    # Create Entry column which consists of the Date and Time columns
    transform_df["Entry"] = pd.to_datetime(transform_df["Date"] + " " + transform_df["Time"], format="mixed")

    transform_df["Entry"] = transform_df["Entry"].dt.strftime("%b %d, %Y - %H:%M:%S")

    # Only get the id, Full Name, Biometrics, and Entry columns for the transformed dataframe
    fullname_df = transform_df.loc[:, ["id", "Full Name", "Biometrics", "Entry"]]

    return fullname_df

# Loading the transformed dataframe to Excel file and formatting the final Excel file
def load_to_excel(dataframe, final_file_path):
    try:
        final_file = final_file_path.replace(".csv", "-CONVERTED.xlsx")

        dataframe.to_excel(final_file, engine="openpyxl", index=False)

        format_excel_file(final_file)
    except PermissionError:
        print("Target Excel file is currently open, please close the file and try again.")

if __name__ == "__main__":
    print("Not to be used on it's own, functions must be imported")
