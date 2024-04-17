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
