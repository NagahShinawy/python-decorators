"""
created by Nagaj at 31/07/2021
"""


def count(function):

    def wrapper():
        text = function()
        return len(text)

    return wrapper


@count
def username():
    return input("Username:")


# ########## ########## ########## ########## ########## #########

def count_2(function):
    txt = function()
    return len(txt)


def username_2():
    return input("username: ")


length = username()
print(length)
print("#" * 100)

ln = count_2(username_2)
print(ln)