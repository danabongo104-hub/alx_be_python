from datetime import datetime, timedelta, date

def display_current_datetime():
    ct = datetime.now()
    format_ct = ct.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {format_ct}")



def calculate_future_date(days):
    future_date = datetime.now() + timedelta(days= days)
    format_future_date = future_date.strftime("%Y-%m-%d %H:%M:%S")  
    print(f"Future date: {format_future_date}")


# Main execution
display_current_datetime()  
date_to_add = int(input("Enter the number of days to add to the current date: "))
calculate_future_date(date_to_add)