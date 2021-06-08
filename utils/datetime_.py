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
    """
    convert days to months
    :param function: any function that return int as days
    :return:
    """

    def wrapper(_date):
        days: int = function(_date)
        months = days // MONTH_DAYS
        reminder = days % MONTH_DAYS
        return {"months": months, "days": reminder}

    return wrapper


def days_to_weeks(function):
    """
        convert days to weeks
        :param function: any function that return int as days
        :return:
    """

    def wrapper(*args, **kwargs):
        days: int = function(*args, **kwargs)
        weeks = days // WEEK_DAYS
        reminder = days % WEEK_DAYS
        return {"weeks": weeks, "days": reminder}

    return wrapper


def validate_quarter(function):
    """
        check if int valid Q [1, 2, 3, 4]
        :param function: any function that return int as Q
        :return:
    """

    def wrapper(*arg, **kwargs):
        quarter: int = function(*arg, **kwargs)
        if 1 <= quarter <= 4:
            return quarter
        raise ValueError("Quarter must be from 1 to 4 , got {}".format(quarter))

    return wrapper


def validate_month(function):
    """
         check if int valid month from 1 to 12
        :param function: any function that return int as month
        :return:
    """

    def wrapper(*arg, **kwargs):
        month: int = function(*arg, **kwargs)
        if 1 <= month <= 12:
            return month
        raise ValueError("Month must be from 1 to 4 , got {}".format(month))

    return wrapper
