import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

# Function to load data from the CSV file
def load_data(filename):
    filename = 'sitka_weather_2018_simple.csv'

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

    # Get dates and high temperatures from this file.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)
    return dates, highs, lows

# Function to plot high temperatures
def plot_highs(dates, highs):
    # Plot the high temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Format plot.
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
# Function to plot low temperatures
def plot_lows(dates, lows):
    # Plot the low temperatures.
    #plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    # Format plot.
    plt.title("Daily low temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

# Main function to run the program and menu
def main():
    print("Sitka Weather Menu")
    print("")
    print("Please select an option:")
    print("Highs: Plot High Temperatures.")
    print("Lows: Plot Low Temperatures.")
    print("Exit: Exit the program.")
    print("")

    filename = 'sitka_weather_2018_simple.csv'
    dates, highs, lows = load_data(filename)

# Input logic for menu selection
    while True:
        choice = input("Enter your choice (Highs, Lows, Exit): ").strip().lower()

        if choice == 'highs':
            plot_highs(dates, highs)
        elif choice == 'lows':
            plot_lows(dates, lows)
        elif choice == 'exit':
            print("Exiting the program.")
            sys.exit()
        else:
            print("Invalid choice. Please enter 'Highs', 'Lows', or 'Exit'.")

# Run the main function
main()