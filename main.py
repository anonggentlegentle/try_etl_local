from etl_funcs import extract_times, transform_name, load_to_csv

time_cols = ["id", "First Name", "Last Name", "Biometrics", "Time", "Date"]

time_path = "C:\\Users\\USER\\Desktop\\03-13-2025.csv"

new_time_path = "C:\\Users\\USER\\Desktop\\03-13-2025-NEW.csv"

df_extract = extract_times(time_path, time_cols)

transformed_df = transform_name(df_extract)

load_to_csv(transformed_df, new_time_path)
