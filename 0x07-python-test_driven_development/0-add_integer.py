#!/usr/bin/python3
"""This defines a function ``add_integer``."""


def add_integer(a, b=98):
    """This functions sums a and b.
    It gives sum(a + b) as output.
    """
    if isinstance(a, int):
        a = a
    elif isinstance(a, float):
        a = int(a)
    else:
        raise TypeError("a must be an integer")

    if isinstance(b, int or float):
        b = b
    elif isinstance(b, float):
        b = int(b)
    else:
        raise TypeError("b must be an integer")

    return (a + b)
