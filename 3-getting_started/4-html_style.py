"""
created by Nagaj at 25/07/2021
"""
from functools import wraps

IMAGE_TAG = '<img src="{src}" alt="{alt}" width="{width}" height="{height}">'
BOLD_TAG = "<b>{content}</b>"
ITALIC_TAG = "<i>{content}</i>"
DIV_TAG = "<div>{content}</div>"


def to_bold_tag(function):
    """
    bold decorators
    :param function:
    :return:
    """
    @wraps(function)  # italic, takes you docs from italic wrapper
    def wrapper():
        """
        from content to bold tag
        :param :
        :return: bold tag
        """
        text = function()
        return f"<b>{text}/b>"

    return wrapper


def to_italic_tag(function):
    """
    italic decorators
    :param function:
    :return:
    """
    @wraps(function)  # function is get_user_name, takes you docs from 'get_user_name'
    def wrapper():
        """
        from content to italic tag
        :param :
        :return: italic tag
        """
        content = function()
        return ITALIC_TAG.format(content=content)

    return wrapper


def to_image_tag(function):
    print("to_image_tag", function)
    """
    decorator docstring
    :return: 
    """

    @wraps(function)  # means update 'wrapper' info to be 'function' info
    def wrapper():
        """
        wrapper docstring
        :return:
        """
        path = function()
        return path
        # return IMAGE_TAG.format(src=path, alt=alt, width=width, height=height)

    # wrapper.__name__ = function.__name__
    # wrapper.__doc__ = function.__doc__
    return wrapper


# @to_italic_tag
# @to_bold_tag
# def get_user_text():
#     """
#     user text
#     :return:
#     """
#     return input("")


@to_bold_tag
@to_italic_tag
def get_user_name():
    """
    user name
    :return:
    """
    return "Smith"


@to_image_tag
def get_image_path():
    """
        image path docstring
        :return:
    """
    return "./images/logo.png"


def upper(function):
    print("upper", function)

    def wrapper():
        text = function()
        return text.upper()

    return wrapper


def username():
    return "john"


if __name__ == "__main__":
    # todo : very important, Decorators in another way
    # todo: Decorators run before function it is decorating is called?
    # TODO:  https://stackoverflow.com/questions/341379/decorators-run-before-function-it-is-decorating-is-called
    # TODO: LOOK AT doc.txt
    # x = upper(username()) # TypeError: 'str' object is not callable
    x = upper(username)  # testing <function username at 0x0000022A2991CEE8>
    print(x)  # <function upper.<locals>.wrapper at 0x0000022A2991CF78>
    print(x())  # JOHN
    # tag = get_user_text()
    # print(tag)
    # print("#" * 100)
    # image = get_image_path()
    # print(image)
    # help(get_image_path)
    print("#" * 100)
    tag = get_user_name()
    print(tag)
    help(get_user_name)
