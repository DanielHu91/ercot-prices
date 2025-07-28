import pandas as pd
import glob
import os
import matplotlib.pyplot as plt

from rename import rename_files
from clean_sheets import clean_sheet

folder_path = '.'
rename_files(folder_path)

excel_files = glob.glob(os.path.join(folder_path, "*.xls")) + \
    glob.glob(os.path.join(folder_path, "*.xlsx"))

def extract_year(file_path):
    filename = os.path.basename(file_path)
    return int(filename[:4])

excel_files.sort(key = extract_year)

dataframes = []

print(f"Found {len(excel_files)} Excel files.\n")
for file in excel_files:
    print(file)
print()

for data in excel_files:
    print(f"Reading {data}...")

    engine = 'openpyxl' if data.endswith('.xlsx') else None
    df = pd.read_excel(data, engine = engine)
    print(df.head())
    print()
    dataframes.append(df)

print(f"Loaded {len(dataframes)} files.")

print("Cleaning data...\n")
df = clean_sheet(dataframes)
df.to_csv('cleaned_data.csv', index=False)