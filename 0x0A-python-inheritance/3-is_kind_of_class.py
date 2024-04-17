#!/usr/bin/python3
"""This module defines a function is_kind_of_class."""


def is_kind_of_class(obj, a_class):
    """Function to check if object of a specified class.
    Args:
        obj: Object to check its type.
        a_class: The object type to check object against.
    Returns:
        True (bool): If object is exactly an instance of the specified class.
        False (bool): If object is not an instance of the specified class.
    """
    return (isinstance(obj, a_class))
