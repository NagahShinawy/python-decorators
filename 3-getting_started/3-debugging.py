from functools import wraps


def make_posh(function):

    def wrapper():
        """
        make it beautiful [wrapper function]
        :return:
        """
        text = function()
        print(f"+{'-' * 10}+")
        print(f"|{' ' * 10}|")
        print(" " * 3, text, " " * 3)
        print(f"|{' ' * 10}|")
        print(f"+{'-' * 10}+")

    return wrapper


def beauty_name(func):
    def wrapper():
        """
        wrapper for name
        :return:
        """
        uname = func()
        return f"<{uname}>"

    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper


def to_upper(func):

    @wraps(func)  # works like [wrapper.__name__ = func.__name__] & [wrapper.__doc__ = func.__doc__]
    def wrapper():
        """
        make it upper
        :return:
        """
        lgs: str = func()
        return lgs.upper()

    # todo : use wraps(func) built in instead
    # wrapper.__name__ = func.__name__
    # wrapper.__doc__ = func.__doc__
    return wrapper


def usertext():

    """
    text to be beauty
    :return:
    """
    return "TEST"


@make_posh
def info():
    """
    info to beauty
    :return:
    """
    return "INFO"


@beauty_name
def name():
    """
    user name Testing John
    :return:
    """
    return "John"


@to_upper
def logs():
    """
    create server logs
    :return:
    """
    return "error"


wrp = make_posh(usertext)
print(wrp)
wrp()

info()

print(usertext.__name__)  # usertext
print(usertext.__doc__)  # function doc string
print(wrp.__name__)  # wrapper
print(info.__name__)  # wrapper

print("#" * 100)

help(usertext)
help(info)  # wrapper

print(name())
help(
    name
)  # name function because it was updated by  wrapper.__name__ = func.__name__ & wrapper.__doc__ = func.__doc__

help(logs)

print(logs.__name__)
print(logs.__doc__)