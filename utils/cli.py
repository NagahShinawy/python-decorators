"""
created by Nagaj at 08/06/2021
"""


def validate_str(function):
    """
       validate string
       :param function: value of string
       :return: valid string not empty and at least 3 chars
    """

    def wrapper(*arg, **kwargs):
        string = function(*arg, **kwargs)
        if string == "":
            raise ValueError("can not be empty")

        if len(string) < 3:
            raise ValueError("short name")
        return string

    return wrapper
