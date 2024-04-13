#!/usr/bin/python3
"""This module defines a class Square."""


class Square:
    """A class representing a squae."""

    def __init__(self, size=0):
        """Initialize the Square instance with a specific size.

        Args:
            size (int): The size of the square's size.
                        Default is 0.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if size != int(size):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        
        self.__size = size
