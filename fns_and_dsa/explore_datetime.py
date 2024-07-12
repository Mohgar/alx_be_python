from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    current_date_formating = current_date.strftime('%Y-%m-%d %H:%M:%S')
    print(f"the current date and time is {current_date_formating}")
display_current_datetime()
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    today = datetime.now()
    future_date = today + timedelta(days= number_of_days)
    print(f"Future date: {future_date}")
calculate_future_date()

