#!/usr/bin/python3
"""Declare a class Square."""


class Square:
    """A square is a four four sided shape.
    It has equal sides."""
    def __init__(self, size=0):
        """Initialize the size of square.
        int(size): size of a side of square."""
        if size != int(size):
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size
