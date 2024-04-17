#!/usr/bin/python3
"""This module defines a function is_kind_of_class."""


def inherits_from(obj, a_class):
    """Function to check if object is of a specified class or
    inherits from it directly or indirectly.
    Args:
        obj: Object to check its a subclass.
        a_class: The object type to check object against.
    Returns:
        True (bool): If object is exactly an instance of the specified class.
        False (bool): If object is not an instance of the specified class.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
