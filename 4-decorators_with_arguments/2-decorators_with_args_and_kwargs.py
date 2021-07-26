"""
created by Nagaj at 26/07/2021
"""
users = ["john", "james", "leon", "smith", "sara"]
MIN_PASSWORD_LENGTH = 8


def validate(function):
    def wrapper(username, password):
        # run something before
        if username in users:
            raise ValueError("Already exist")
        if len(password) < 8:
            raise ValueError(f"Password should be at least {MIN_PASSWORD_LENGTH} ")
        function(username, password)
        # run something after

    return wrapper


@validate
def create(username, password):
    print(f"user <{username}> created! with password HASHED{password}HASHED")


create("Jose", "342342TEST")
