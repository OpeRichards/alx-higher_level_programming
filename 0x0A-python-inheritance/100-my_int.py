#!/usr/bin/python3
"""This module defines a class MyInt."""


class MyInt(int):
    """This module defines class MyInt which
    inherits from int.
    Returns:
        (==) __eq__ : Make equal to act as not equal.   .
        (!=) __ne__ : Make not equal to act as equal.
    """
    def __eq__(self, varb):
        return not super().__eq__(varb)

    def __ne__(self, varb):
        return not super().__ne__(varb)
