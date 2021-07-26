"""
created by Nagaj at 26/07/2021
"""


def pfib(a, b, c):
    print(a, b, c)


def themes(color="white", *args):
    print(color)
    if args:
        print(args)


def table_style(**kwargs):
    print(kwargs)


def calc_deps_cost(hr, accounting, it):
    return hr + accounting + it


def calc_deps_revenue(hr, accounting, it):
    return hr + accounting + it


def create(username, password, email):
    print(f"added username <{username}> with password <{password}> and email <{email}>")


def welcome_back(*args, **kwargs):
    welcome = "Welcome Back " + " ".join(args)

    if not kwargs:
        return welcome

    msg = "\nYou Have:\n"
    for key, value in kwargs.items():
        info = f"{key}: {value}\n"
        msg += info

    message = welcome + msg
    return message


pfib(1, 6, 8)

# themes("red", color="blue") # TypeError: themes() got multiple values for argument 'color'
themes("blue", "black", "white", "red")

table_style(color="white", bg="red", font="source code")

total = [10, 70, 20]

print(calc_deps_cost(*total))  # unpacking
print(calc_deps_cost(1, 5, 6))

deps = {"hr": 30, "accounting": 50, "it": 100}

print(calc_deps_revenue(**deps))  # unpacking

data = {"username": "john", "password": "test", "email": "john@test.edu"}

# create(username="james", password="ja1234", email="james@unv.edu")
create(username=data["username"], password=data["password"], email=data["email"])

create(**data)

wlc = welcome_back("John", "Leon", "(+9)", notifacation=3, inbox=50, missed_calls=10)
print(wlc)
