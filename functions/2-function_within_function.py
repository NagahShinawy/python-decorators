"""
created by Nagaj at 13/07/2021
"""


def fib_three(a, b, c):
    def get_three():  # inner function
        # print(a, b, c)
        return a, b, c

    return get_three


function = fib_three(4, 6, 7)  # fib_three returns func obj
print(function)

numbers = function()  # so, function obj can be callable. function() returns numbers
print(numbers)
a, *others = numbers  # unpacking just 'a' and packing other numbers to 'others'
print(a)
print(others)
