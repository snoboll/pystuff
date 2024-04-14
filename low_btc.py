import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

def fetch_data(start, end):
    """Fetch historical Bitcoin prices using yfinance."""
    try:
        data = yf.download('BTC-USD', start=start, end=end)
        return data
    except Exception as e:
        print(f"Failed to fetch data: {e}")
        return None

def calculate_daily_averages(df):
    """Calculate average closing prices for each day of the month across all years."""
    df['DayOfMonth'] = df.index.day
    return df.groupby('DayOfMonth')['Close'].mean()

def plot_data(average_prices):
    """Plot the average closing prices by day of the month."""
    plt.figure(figsize=(14, 7))
    plt.plot(average_prices.index, average_prices.values, marker='o', linestyle='-')
    plt.title('Average Bitcoin Closing Prices by Day of the Month')
    plt.xlabel('Day of the Month')
    plt.ylabel('Average Price (USD)')
    plt.xticks(range(1, 32))  # Ensure all days are shown
    plt.grid(True)
    plt.show()

start_date = datetime(2014, 1, 1)
end_date = datetime(2023, 12, 31)

# Fetch the data
bitcoin_data = fetch_data(start_date, end_date)

# Calculate daily averages across all years
if bitcoin_data is not None:
    daily_averages = calculate_daily_averages(bitcoin_data)
    plot_data(daily_averages)

    # Find the cheapest day and calculate the advantage of DCA
    cheapest_day = daily_averages.idxmin()
    cheapest_price = daily_averages.min()
    overall_average = daily_averages.mean()
    
    # Calculate the advantage of buying on the cheapest day
    advantage_percent = ((overall_average - cheapest_price) / overall_average) * 100

    # Rank the top 5 cheapest days
    sorted_days = daily_averages.sort_values()
    days = sorted_days.head(30)


    top_5_advantages = ((overall_average - days) / overall_average) * 100

    print(f"The best day of the month to buy Bitcoin is the {cheapest_day}th, with an average price advantage of {advantage_percent:.2f}% over a random day.")
    print("Top 5 days to buy Bitcoin based on historical data and their advantages:")
    for day, advantage in zip(days.index, top_5_advantages):
        print(f"Day {day}: {advantage:.2f}% advantage")



else:
    print("Failed to fetch data.")
