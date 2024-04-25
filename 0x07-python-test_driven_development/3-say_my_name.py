#!/usr/bin/python3
"""This module defines function ``say_my_name``."""


def say_my_name(first_name, last_name=""):
    """Function that prints a string.
    Args:
        first_name (string): First name of a person.
        last_name (string): (Optional) Surname of a person.
    Prints:
        string: My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
