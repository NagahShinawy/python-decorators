"""
created by Nagaj at 13/07/2021
"""


def printfib():
    """
    Print Fibonacci
    :return:
    """

    print("Fibonacci")


def printfib2():
    """
    Print Fibonacci
    :return:
    """

    return "Fibonacci"


#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34
def fibonacci(number):
    first = counter = 0
    second = first + 1
    while counter <= number:

        if counter <= 1:
            total = 1
            print(total, end=" ")
        else:
            total = first + second
            print(total, end=" ")
        first = second
        second = total
        counter += 1


def fibonacci2(number):
    if number < 2:
        return number
    return fibonacci2(number - 1) + fibonacci2(number - 2)


if __name__ == "__main__":
    # every thing in python is an object
    print(printfib)  # function obj at 0x0000023DBDBB2828
    print(type(printfib))  # <class 'function'>
    print(printfib.__class__)  # <class 'function'>
    print(type(printfib()))  # run function, then print type for [output] = [NoneType]

    printfib()

    print("#" * 100)
    print(printfib2)  # <function printfib2 at 0x00000241AA697168>
    print(printfib2.__class__)  # <class 'function'>
    print(printfib2())  # Fibonacci
    fib = printfib2()
    print(fib.__class__)  # <class 'str'>
    print(type(fib))  # <class 'str'>
    print(type(fib.__class__))  # <class 'type'>
    print("".__class__)  # <class 'str'>

    print("#" * 100)
    fibonacci(10)
    print()
    print(fibonacci2(5))
