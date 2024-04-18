#!/usr/bin/python3
"""This function defines add_attribute."""


def add_attribute(obj, attr, value):
    """This function adds a new attribute to an object (where possible).
    Args:
        obj (any): The object to add an attribute to.
        attr (str): The name of the attribute to add to obj.
        value (any): The value of attr.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")

    setattr(obj, attr, value)
