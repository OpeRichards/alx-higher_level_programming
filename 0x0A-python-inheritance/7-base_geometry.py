#!/usr/bin/python3
"""This module defines a class BaseGeometry."""


class BaseGeometry:
    """This is class BaseGeometry."""
    def area(self):
        """Raise exception."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """This method validates value.
        Args:
            name (str): Name object to validate.
            value (int): Integer to validate.
        Returns:
            ValueError: Raise ValueError Exception.
            TypeError: Raise TypeError Exception.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
