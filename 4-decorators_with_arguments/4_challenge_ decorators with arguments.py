"""
created by Nagaj at 26/07/2021
"""

PUNCTUATION = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""


def punctuation(function):
    def wrapper(text: str):
        counts = 0
        for char in text:
            if char in PUNCTUATION:
                counts += 1
        function(text)
        return counts
    return wrapper


@punctuation
def user_feedback(text):
    print(f"Feedback <{text}> was sent")
    print("Thanks for you feedback")


punc = user_feedback("good service! go on.")
print(punc)