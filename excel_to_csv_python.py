import pandas as pd

# specify path of the Excel spreadsheet file
file_path = "some_file.xlsx"

# read the Excel spreadsheet into a Data Frame
df = pd.read_excel(file_path)

# specify the file path for the CSV file
csv_file = "example.csv"

# write the DataFrame to a CSV file
df.to_csv(csv_file, index=False)
