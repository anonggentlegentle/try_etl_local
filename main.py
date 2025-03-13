from etl_funcs import extract_times, transform_name, load_to_excel
from excel_formatting import format_excel_file

time_cols = ["id", "First Name", "Last Name", "Biometrics", "Time", "Date"]

file = "03-13-2025"

time_path = f"C:\\Users\\USER\\Desktop\\{file}.csv"

new_time_path = f"C:\\Users\\USER\\Desktop\\{file}-NEW.xlsx"

df_extract = extract_times(time_path, time_cols)

transformed_df = transform_name(df_extract)

load_to_excel(transformed_df, new_time_path)

format_excel_file(new_time_path)