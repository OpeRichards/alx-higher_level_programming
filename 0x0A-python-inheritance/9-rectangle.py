#!/usr/bin/python3
"""This module defines a class BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This module defines class Rectangle which
    inherits from BaseGeometry."""
    def __init__(self, width, height):
        """Initialize the class Rectangle.
        Args:
            Width (int): Size of one side of a rectangle.
            Height (int): Size of adjacent side.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """This method defines the area of the rectangle.
        Args:
            self.__width (int)
            self.__height (int)
        Returns:
            area (int): Result of multiples of both sides.
        """
        area = self.__width * self.__height
        return area

    def __print__(self):
        """This method calls the print function to print."""
        print()

    def __str__(self):
        """This method returns a specified string output."""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
