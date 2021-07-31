"""
created by Nagaj at 31/07/2021
"""
"""
created by Nagaj at 31/07/2021
"""

# https://stackoverflow.com/questions/7492068/python-class-decorator-arguments


class Validate:

    def __init__(self, function, ln):
        self.function = function
        self.ln = ln

    def __call__(self, sha):
        text = self.function(sha)
        if len(text) < self.ln:
            raise ValueError(f"pwd can not be less than {self.ln} chars")
        print("Your Password is safe")
        return text

    def __str__(self):
        return f"Validate({self.function.__name__})"


def pwd(sha):
    if sha == 16:
        return "534534<16>"
    elif sha == 265:
        return "534534<265>"
    return f"348998543534<{sha}>"


validated_pwd = Validate(pwd, ln=10)(sha=20)
print(validated_pwd)
# print(validated_pwd())

