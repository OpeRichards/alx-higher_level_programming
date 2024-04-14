#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """A class representing a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square instance with a specific size.
        Args:
            size (int): The size of the square's size.
                        Default is 0.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
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

    @property
    def position(self):
        """Get the position of the square,
        using coordinates"""
        return self.__position

    @position.setter
    def size(self, value):
        """Set the position of the square.
        Args:
            value (tuple): The new position of the square.
        Raises:
            TypeError: If value is not a tuple of 2 integers 
            or contains negative values.
        """
        if len(value) != 2 or not isinstance(value, tuple) or \
            not all(isinstance(num, int) for num in value) or \
            any(num < 0 for num in value):
            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = position

    def area(self):
        """Calculate the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using # character."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print('')
            for i in range(self.__size):
                print(' ' * self.__position[0] + "#" * self.__size)
