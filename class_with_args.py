"""
created by Nagaj at 31/07/2021
"""

# https://stackoverflow.com/questions/7492068/python-class-decorator-arguments

PUNCTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""


def count_punctuation(function):
    def wrapper(text: str):
        counts = 0
        for char in text:
            if char in PUNCTUATION:
                counts += 1
        function(text)
        return counts

    return wrapper


@count_punctuation
def user_feedback(text):
    print(f"Feedback <{text}> was sent")
    print("Thanks for you feedback")


# user_feedback("nagah")

print("#####################################")
# ############# ############# ############# ############# ############# ############


class Validate:

    def __init__(self, function, ln=8):
        self.function = function
        self.ln = ln

    def __call__(self, *args, **kwargs):
        text = self.function(*args, **kwargs)
        if len(text) < self.ln:
            raise ValueError(f"pwd can not be less than {self.ln} chars")
        print("Your Password is safe")
        return text

    def __str__(self):
        return f"Validate({self.function.__name__})"


def validate_this(ln):
    def _validate(func):
        return Validate(func, ln)
    return _validate


@validate_this(6)
def pwd():
    return "pwd2342"


x = pwd
print(x)
x()
