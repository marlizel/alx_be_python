from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date  # We return it so we can use it in the next function

def calculate_future_date(current_date):
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)
    print("Future date:", future_date.strftime("%Y-%m-%d %H:%M:%S"))

# Run the functions
current = display_current_datetime()
calculate_future_date(current)
