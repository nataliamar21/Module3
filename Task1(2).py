import datetime

def get_days_from_today(date):
    try:
        
        input_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.datetime.today().date()
        delta = current_date - input_date
        
        return delta.days
    
    except ValueError:
        print("Incorrect date format.Use the format'YYYY-MM-DD'.")
        return None

date_str=input("Enter date in 'YYYY-MM-DD':")
print(get_days_from_today(date_str))