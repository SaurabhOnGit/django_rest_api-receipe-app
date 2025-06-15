"""calculator.py
A simple calculator module that provides basic arithmetic operations.
"""


def add(x, y):
    """_summary_

    Args:
        x (_type_): first number
        y (_type_): second number

    Returns:
        _type_: addition of the numbers
    """
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    else:
        raise ZeroDivisionError("not allow to divide by zero")
