#!/usr/bin/python3
"""This module defines a class Square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This module defines class Square which
    inherits from Rectangle and a grandchild to BaseGeometry"""
    def __init__(self, size):
        """Initialize the class Square.
        Args:
            size (int): The length of each side of a square.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """This method defines the area of the rectangle.
        Args:
            self.__width (int)
            self.__height (int)
        Returns:
            area (int): Result of multiples of both sides.
        """
        area = self.__size ** 2
        return area

    def __str__(self):
        """This method returns a specified string output."""
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
