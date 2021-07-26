"""
created by Nagaj at 26/07/2021
"""
from time import perf_counter
from functools import wraps


users = ["john", "james", "leon", "smith", "sara"]
MIN_PASSWORD_LENGTH = 8
total_duration = 0


def timer(function):

    @wraps(function)
    def wrapper(*args, **kwargs):
        global total_duration
        start = perf_counter()
        result = function(*args, **kwargs)
        end = perf_counter()
        duration = end - start
        total_duration += duration
        print(f"{function.__name__}{args} = {result} -> {duration:.8f}s")
        # print("Duration: {:.2f}".format(duration))
        return result
    return wrapper


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


@timer
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@validate
def create(username, password):
    print(f"user <{username}> created! with password HASHED{password}HASHED")


create("Jose", "342342TEST")

num = fib(20)
print(num)
print("Total Duration {:.2f}s".format(total_duration))
