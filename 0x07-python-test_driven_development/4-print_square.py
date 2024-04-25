#!/usr/bin/python3
"""This module defines function ``print_square``."""


def print_square(size):
    """Function that prints a square with charcter #.
    Args:
        size (int): Indicates size of each side of the square.
    Prints:
        A square of size `size`.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            print("#" * size)
