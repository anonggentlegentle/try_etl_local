from etl_funcs import extract_times, transform_name, load_to_excel
from excel_formatting import format_excel_file
import tkinter as tk
from tkinter.filedialog import askopenfilename, askdirectory

while True:
    try:
        # print("Enter the CSV filename in 'MM-DD-YYYY' format :")
        # file_name = input()

        time_cols = ["id", "First Name", "Last Name", "Biometrics", "Time", "Date"]

        # time_path = f"C:\\Users\\USER\\Desktop\\{file_name}.csv"

        # new_time_path = f"C:\\Users\\USER\\Desktop\\{file_name}-NEW.xlsx"

        file_path = askopenfilename().replace("/", "\\")

        final_file_path = file_path.replace("/", "\\")

        df_extract = extract_times(file_path, time_cols)

        transformed_df = transform_name(df_extract)

        load_to_excel(transformed_df, final_file_path)
    except FileNotFoundError:
        print(f"The CSV file named cannot be found. Please enter a filename again.")
        continue
    else:
        break