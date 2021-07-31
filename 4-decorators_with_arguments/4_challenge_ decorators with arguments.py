"""
created by Nagaj at 26/07/2021
"""
from functools import wraps


PUNCTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""


def remove_punctuation(function):
    def wrapper(text: str):
        counts = 0
        for char in text:
            if char in PUNCTUATION:
                counts += 1
        function(text)
        return counts

    return wrapper


def munch(start, end):

    def do_munch(function):
        @wraps(function)
        def wrapper():
            text = function()
            staring_text = text[:start]
            xs = "X" * (end - start)
            ending_text = text[end:]
            result = staring_text + xs + ending_text

            return result
        return wrapper
    return do_munch


def munch2(function):
    def wrapper2():
        text = function()
        return text
        # if len(args) != 2:
        #     return text
        # start, end = args
        # staring_text = text[:start]
        # xs = "X" * (end - start)
        # ending_text = text[end:]
        # result = staring_text + xs + ending_text

        return result
    return wrapper2


@remove_punctuation
def user_feedback(text):
    print(f"Feedback <{text}> was sent")
    print("Thanks for you feedback")


@munch(2, 5)
def fullname():
    return "John James Leon"


# @munch2(2, 5)
# def fullname2():
#     return "John James Leon"


def munch3(function, start, end):
    print(start, end)
    text = function()
    staring_text = text[:start]
    xs = "X" * (end - start)
    ending_text = text[end:]
    result = staring_text + xs + ending_text
    return result


def fullname3():
    return "John"


punc = user_feedback("good service! go on. hope to see new features soon ^_^")
print(punc)

print("#" * 100)
print(fullname())
# print(fullname2())

print("#" * 100)
john = munch3(fullname3, 2, 3)
print(john)