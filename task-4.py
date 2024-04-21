from datetime import datetime, timedelta


def get_upcoming_birthdays(users: dict) -> dict:
    # current date
    today = datetime.today().date()

    birthday_list = []

    # convert to datetime object
    for user in users:

        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_to_birthday = (birthday_this_year - today).days

        if 0 <= days_to_birthday < 7:

            if birthday_this_year.weekday() >= 5:
                days_to_birthday += 7 - birthday_this_year.weekday()

            # add current birthday to the new list
            congratulation_date = today + timedelta(days=days_to_birthday)

            birthday_list.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return birthday_list


users = [
    {"name": "Jack", "birthday": "1982.04.27"},
    {"name": "Evan", "birthday": "2000.06.25"},
    {"name": "Tom", "birthday": "1995.04.25"},
    {"name": "Mac", "birthday": "1972.01.01"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
