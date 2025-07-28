import pandas as pd
import glob

def clean_sheet(file_paths):
    all_data = []

    for df in file_paths:
        df = df[df['Settlement Point Name'].str.endswith('AVG')]

        df['Delivery Date'] = pd.to_datetime(df['Delivery Date'])
        df['Delivery Hour'] = df['Delivery Hour'].astype(int) - 1
        df['Delivery Interval'] = df['Delivery Interval'].astype(int)

        df['Timestamp'] = df['Delivery Date'] + pd.to_timedelta(df['Delivery Hour'], unit='h') + pd.to_timedelta((df['Delivery Interval'] - 1) * 15, unit = 'min')

        all_data.append(df)

    combined_df = pd.concat(all_data, ignore_index=True)
    combined_df.to_csv('cleaned_data.csv', index=False)
    print("Data cleaned and saved to 'cleaned_data.csv'.")
    print(combined_df.head(10))

    combined_df['Hour'] = combined_df["Timestamp"].dt.floor('h')

    hourly_avg = (
        combined_df.groupby(['Hour', 'Settlement Point Name']) ['Settlement Point Price']
        .mean()
        .reset_index()
        .rename(columns={'Hour': 'Timestamp', 'Settlement Point Price': 'Hourly Average Price'})
    )

    hourly_avg.to_csv('hourly_avg_prices.csv', index=False)
    print("Hourly averages calculated and saved to 'hourly_avg_prices.csv'.")
    print(hourly_avg.head(10))