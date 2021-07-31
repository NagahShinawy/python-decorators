"""
created by Nagaj at 31/07/2021
"""
from functools import update_wrapper


def count(function):
    def wrapper():
        text = function()
        return len(text)

    return wrapper


@count
def username():
    return "John"


# ########## ########## ########## ########## ########## #########

def count_2(function):
    txt = function()
    return len(txt)


def username_2():
    return "James"


# ########## ########## ########## ########## ########## #########

class Count:

    def __init__(self, func):
        update_wrapper(self, func)  # act like wraps
        self.func = func
        # self.count = 0

    def __call__(self, *args, **kwargs):  # act like wrapper
        # self.count += 1
        # print(f"Current Count: {self.count}")
        text = self.func(*args, **kwargs)
        return len(text)


# ########## ########## ########## ########## ########## #########


class Validate:

    def __init__(self, function):
        update_wrapper(self, function)  # act like wraps
        self.function = function

    def __call__(self, *args, **kwargs):
        text = self.function(*args, **kwargs)
        if len(text) < 8:
            raise ValueError("pwd can not be less than 8 chars")
        print("Your Password is safe")
        return text


length = username()
print(length)
print("#" * 100)

ln = count_2(username_2)
print(ln)
print("#" * 100)


# ########## ########## ########## ########## ########## #########


@Count
def password():
    """
    get user password
    :return:
    """
    return "P@assw0rd123"


def password2():
    return "Mypwd77"


@Validate
def password3():
    """
    user password
    :return:
    """
    return "gdfmgdfm#534534m$^%^$^#^"


pwd = password()
print(pwd)

# ########## ########## ########## ########## ########## #########
print("#" * 100)

ctn = Count(password2)
ln = ctn()
print(ln)

# ########## ########## ########## ########## ########## #########
print("#" * 100)

pwd = password3()
print(pwd)
print(password3.__doc__)
