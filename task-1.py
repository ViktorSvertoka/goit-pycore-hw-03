from datetime import datetime


def get_days_from_today(date):
    try:
        # We convert the date string in the format 'YYYY-MM-DD' into a datetime object
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        # We get the current date
        current_date = datetime.today()
        # We calculate the difference between the current date and the specified date
        difference = current_date - date_obj
        # Return the difference in days as an integer
        return difference.days
    except ValueError:
        return "Invalid date format. Enter date in 'YYYY-MM-DD' format."


print(get_days_from_today("1987-10-03"))
