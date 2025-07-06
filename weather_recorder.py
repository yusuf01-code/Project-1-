import pandas as pd
from datetime import datetime

# Data storage
weather_data = []
dates_set = set()

# Function to validate date
def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Function to add weather data
def add_weather_data():
    date = input("Enter date (YYYY-MM-DD): ")
    if not is_valid_date(date):
        print("Invalid date format!")
        return

    if date in dates_set:
        print("Duplicate date! Entry already exists.")
        return

    try:
        temperature = float(input("Enter temperature (°C): "))
    except ValueError:
        print("Invalid temperature!")
        return

    condition = input("Enter weather condition (e.g., sunny, rainy): ")

    weather_data.append({
        "Date": date,
        "Temperature": temperature,
        "Condition": condition
    })
    dates_set.add(date)
    print("Weather data added successfully.\n")

# Function to view weather data
def view_data():
    if not weather_data:
        print("No data available.\n")
        return
    df = pd.DataFrame(weather_data)
    print(df.to_string(index=False))

# Function to export to CSV
def export_to_csv():
    if not weather_data:
        print("No data to export.\n")
        return
    df = pd.DataFrame(weather_data)
    df.to_csv("weather_data.csv", index=False)
    print("Data exported to weather_data.csv\n")

# Function to show average temperature
def show_average_temperature():
    if not weather_data:
        print("No data available.\n")
        return
    df = pd.DataFrame(weather_data)
    avg_temp = df["Temperature"].mean()
    print(f"Average Temperature: {avg_temp:.2f}°C\n")

# Menu
def menu():
    while True:
        print("=== Weather Data Recorder ===")
        print("1. Add Weather Data")
        print("2. View All Data")
        print("3. Show Average Temperature")
        print("4. Export to CSV")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            add_weather_data()
        elif choice == "2":
            view_data()
        elif choice == "3":
            show_average_temperature()
        elif choice == "4":
            export_to_csv()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    menu()
