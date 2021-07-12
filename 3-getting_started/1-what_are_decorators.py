"""
created by Nagaj at 13/07/2021
"""


def to_title(function):
    def wrapper():
        name: str = function()
        return name.title()

    return wrapper


def to_lower(function):
    def wrapper():
        text: str = function()
        return f"Changing [{text}] to lower[{text.lower()}]"

    return wrapper


def my_decorator(function):
    """
    Decorator
    :param function:
    :return:
    """

    def wrapper():
        fib = function()
        return "-".join(list(fib))

    return wrapper


@my_decorator  # apply decorator to function
def pfib():
    """
    Fibonacci
    :return:
    """
    return "Fibonacci"


@to_title  # apply decorator to function
def username():
    return "john smith"


@to_lower  # apply decorator to function
def header():
    return "THIS IS HEADER"


print(pfib())
user_name = username  # <function to_title.<locals>.wrapper at 0x000002497682BC18>
print(user_name)
print(user_name())  # <function to_lower.<locals>.wrapper at 0x000002497682BD38>

post = header
print(post)
print(post())

print("#" * 100)


def to_egp(function):
    def wrapper():
        salary = function()
        return salary * 15

    return wrapper


def get_dollar_salary():
    return float(input("salary:"))


emp_salary = to_egp(get_dollar_salary)  # <function to_egp.<locals>.wrapper at 0x0000024E4F1710D8>

print(emp_salary)

print(emp_salary())
