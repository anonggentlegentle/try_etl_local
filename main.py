from etl_funcs import extract_times, transform_name, load_to_excel
from excel_formatting import format_excel_file
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory

while True:
    try:
        # Defining the rows of the dataframe
        time_cols = ["id", "First Name", "Last Name", "Biometrics", "Time", "Date"]

        # Defining the paths of the file to transform and the final file
        file_path = askopenfilename().replace("/", "\\")

        final_file_path = file_path.replace("/", "\\")

        # Executing the functions to extract data, transform data, load and format the final excel file
        df_extract = extract_times(file_path, time_cols)

        transformed_df = transform_name(df_extract)

        load_to_excel(transformed_df, final_file_path)
    except FileNotFoundError:
        print(f"The CSV file named cannot be found. Please enter a filename again.")
        continue
    else:
        break