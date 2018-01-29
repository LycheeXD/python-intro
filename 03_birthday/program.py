import datetime

def print_header():
    print('------------------------')
    print('        birthday')
    print('------------------------')


# function declaration - def function_name(parameter):
def get_birthday_from_user():
    # defines a function but not ready to implement yet - pass
    print('when were you born? ')
    year = int(input('year [YYYY]: '))
    month = int(input('month [MM]: '))
    day = int(input('day [DD]: '))

    birthday = datetime.date(year, month, day)

    return birthday


# 2 lines between 2 functions that are standalone functions (PEP8)
def compute_days_between_dates(birthday_date, today_date):
    this_year_birthday_date = datetime.date(today_date.year, birthday_date.month, birthday_date.day)

    days_between_dates = this_year_birthday_date - today_date

    return days_between_dates.days


def print_birthday_information(days_until_birthday):
    if days_until_birthday < 0:
        print('bday was {} days ago'.format(-days_until_birthday))
    elif days_until_birthday > 0:
        print('bdays is {} days away'.format(days_until_birthday))
    else:
        print('happy birthday')


def main():
    print_header()

    users_birthday = get_birthday_from_user()
    todays_date = datetime.date.today()

    days_until_birthday = compute_days_between_dates(users_birthday, todays_date)

    print_birthday_information(days_until_birthday)


main()