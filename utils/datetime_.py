"""
created by Nagaj at 08/06/2021
"""

from datetime import date

today = date.today()

DEC = 12
DAYS_OF_DEC = 31
WEEK_DAYS = 7
MONTH_DAYS = 30


def days_to_month(function):
    def wrapper(_date):
        days: int = function(_date)
        months = days // MONTH_DAYS
        reminder = days % MONTH_DAYS
        return {"months": months, "days": reminder}

    return wrapper


def days_to_weeks(function):
    def wrapper(*args, **kwargs):
        days: int = function(*args, **kwargs)
        weeks = days // WEEK_DAYS
        reminder = days % WEEK_DAYS
        return {"weeks": weeks, "days": reminder}

    return wrapper


def validate_quarter(function):
    def wrapper(*arg, **kwargs):
        quarter: int = function(*arg, **kwargs)
        if 1 <= quarter <= 4:
            return quarter
        raise ValueError("Quarter must be from 1 to 4 , got {}".format(quarter))

    return wrapper


def validate_month(function):
    def wrapper(*arg, **kwargs):
        month: int = function(*arg, **kwargs)
        if 1 <= month <= 12:
            return month
        raise ValueError("Month must be from 1 to 4 , got {}".format(month))

    return wrapper
