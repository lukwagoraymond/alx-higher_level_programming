#!/usr/bin/python3
"""
    0_add_integer module
    This function adds two numbers
    returns a + b
"""


def add_integer(a, b=98):
    """Function that adds 2 integers
    Args:
        a (int): The first integer
        b (int): The second integer
    Returns:
        a + b
    """
    if not (type(a) is int or type(a) is float):
        raise TypeError("a must be an integer")
    elif not (type(b) is int or type(b) is float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
