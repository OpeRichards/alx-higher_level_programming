#!/usr/bin/python3
"""This module creates a class MyList."""


class MyList(list):
    """A class MyList that inherits from class list."""
    def print_sorted(self):
        """Sorts a list in ascending order.
        Returns:
            sorted list (int): Sorted list.
        """
        print(sorted(self))
