"""
created by Nagaj at 25/07/2021
"""
from functools import wraps


def bold(function):
    """
    Bold decorator
    :param function:
    :return:
    """

    @wraps(function)
    def wrapper():
        """
        :return: html bold tags
        """
        content = function()
        return f"<b>{content}</b>"

    return wrapper


def italic(function):
    """
    italic decorator
    :param function:
    :return:
    """

    @wraps(function)
    def wrapper():
        """
        :return: html italic tags
        """
        content = function()
        return f"<i>{content}</i>"

    return wrapper


@bold
@italic
def printfib():
    """
    return Fibonacci
    :return:
    """
    return "Fibonacci"


# todo #1:
# print(printfib())  # without decorator ==>  'Fibonacci'

# todo #2:
# because we are using 'wraps(function)'. output is '<function printfib at 0x0000020DD7284708>'
# without 'wraps(function)' . output will be '<function bold.<locals>.wrapper at 0x000001BEC2F44708>'
print(printfib)

# todo #3:

# <b>Fibonacci</b>
print(printfib())  # actually run function with its decorator 'bold'

# todo #4: order of decorators are very important
# run function with 2 decorators [bold & italic] so, decorate function with 'bold' FIRST then 'italic'
# run FROM top to down
# @bold
# @italic
# means run bold first then italic
# 1-go to bold
# 2-then italic
# 3- get output from 'italic func' returns back to 'bold func'.
# 4- bold run functionality for output of 'italic'
# 5- then return output of italic & bold to 'printfib' function call
# print(printfib())
# <i><b>Fibonacci</b></i>
