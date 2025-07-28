import pandas as pd

def clean_sheet(file_paths):
    all_data = []

    for df in file_paths:

       # sheets = pd.read_excel(file_path, sheet_name=None)
        # df = pd.concat(sheets.values(), ignore_index=True)

        df = df[df['Settlement Point Type'] == 'LZ']

        df['Delivery Date'] = pd.to_datetime(df['Delivery Date'])
        df['Delivery Hour'] = df['Delivery Hour'].astype(int) - 1
        df['Delivery Interval'] = df['Delivery Interval'].astype(int)

        df['Timestamp'] = df['Delivery Date'] + pd.to_timedelta(df['Delivery Hour'], unit='h') + pd.to_timedelta((df['Delivery Interval'] - 1) * 15, unit = 'min')

        all_data.append(df)

    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df