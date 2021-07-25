"""
created by Nagaj at 25/07/2021
"""
IMAGE_TAG = '<img src="{src}" alt="{alt}" width="{width}" height="{height}">'
BOLD_TAG = "<b>{content}</b>"
ITALIC_TAG = "<i>{content}</i>"
DIV_TAG = "<div>{content}</div>"


def to_bold_tag(function):

    def wrapper():
        text = function()
        return f"<b>{text}/b>"

    return wrapper


def to_italic_tag(function):

    def wrapper():
        content = function()
        return ITALIC_TAG.format(content=content)

    return wrapper


def to_image_tag(function):

    def wrapper():
        path = function()
        return path
        # return IMAGE_TAG.format(src=path, alt=alt, width=width, height=height)

    return wrapper


@to_italic_tag
@to_bold_tag
def get_user_text():
    return input("")


@to_bold_tag
@to_italic_tag
def get_user_name():
    return input("name:")


@to_image_tag
def get_image_path():
    return input("path:")


if __name__ == '__main__':
    tag = get_user_text()
    print(tag)
    print("#" * 100)
    image = get_image_path()
    print(image)
    print("#" * 100)
    tag = get_user_name()
    print(tag)