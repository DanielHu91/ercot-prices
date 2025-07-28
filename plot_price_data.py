import matplotlib.pyplot as plt
import pandas as pd

def plot_price_data(file_path='cleaned_data.csv'):
    df = pd.read_csv(file_path)

    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    pivot_df = df.pivot_table(index = 'Timestamp', columns = 'Settlement Point Name', values = 'Settlement Point Price')

    plt.figure(figsize=(18,9))
    for col in pivot_df.columns:
        plt.plot(pivot_df.index, pivot_df[col], label=col)

    plt.xlabel('Time')
    plt.ylabel('Settlement Price ($/MWh)')
    plt.title('ERCOT 15-Minute Interval Prices (2010-2025)')
    plt.legend(title = 'Zone', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.subplots_adjust(right=2)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_price_data()