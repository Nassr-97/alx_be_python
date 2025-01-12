from datetime import datetime, timedelta


# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print(f"Current Date and Time: {formatted_date}")


# Part 2: Calculate a Future Date
def calculate_future_date():
    try:
        # Prompt the user for the number of days
        number_of_days = int(input("Enter the number of days to calculate the future date: "))

        # Calculate the future date
        current_date = datetime.now()  # Get the current date and time
        future_date = current_date + timedelta(days=number_of_days)  # Add days

        # Format and display the future date
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"The date {number_of_days} days from today will be: {formatted_future_date}")
    except ValueError:
        print("Please enter a valid integer for the number of days.")


# Main function to execute both parts
def main():
    print("Part 1: Display the Current Date and Time")
    display_current_datetime()
    print("\nPart 2: Calculate a Future Date")
    calculate_future_date()


if __name__ == "__main__":
    main()
