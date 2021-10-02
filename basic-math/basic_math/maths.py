"""
Starting with the most basic testing problem first (to warm up)
"""

from numbers import Number


def check_two_numeric_inputs(func):
    """
    Used a decorator here to reduce code duplication across all the
    basic math methods.
    """

    def wrapper(*args):
        a_t = type(args[0])
        b_t = type(args[1])
        if (a_t == float or a_t == int) and (b_t == float or b_t == int):
            output = func(*args)
            return output
        else:
            raise ValueError("Both inputs must be numeric.")

    return wrapper


@check_two_numeric_inputs
def add(a: Number, b: Number) -> Number:
    return a + b


@check_two_numeric_inputs
def subtract(a: Number, b: Number) -> Number:
    return a - b


@check_two_numeric_inputs
def multiply(a: Number, b: Number) -> Number:
    return a * b


@check_two_numeric_inputs
def divide(a: Number, b: Number) -> Number:
    return a / b
