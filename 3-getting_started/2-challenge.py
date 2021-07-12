"""
created by Nagaj at 13/07/2021
"""


def make_posh(function):
    def wrapper():
        text = function()
        print(f"+{'-' * 10}+")
        print(f"|{' ' * 10}|")
        print(" " * 3, text, " " * 3)
        print(f"|{' ' * 10}|")
        print(f"+{'-' * 10}+")

    return wrapper


def usertext():
    return "TEST"


@make_posh
def info():
    return "INFO"


wrp = make_posh(usertext)
print(wrp)
wrp()

info()