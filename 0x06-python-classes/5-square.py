#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        """Initialize the Square instance with a specific size.
        Args:
            size (int): The size of the square's size.
                        Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size

    @property
    def size(self, value):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """set the size of the square.
        Args:
            value (int): The size of the square's size.
                        Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if value != int(value):
            raise TypeError('size must be an integer')

        if value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """Calculate the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # character."""
        for i in range(self.__size):
            if self.__size > 0:
                print("#" * self.__size)
            else:
                print()
