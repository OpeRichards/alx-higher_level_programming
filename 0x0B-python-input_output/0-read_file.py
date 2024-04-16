#!/usr/bin/python3
"""Define a function read_file"""


def read_file(filename=""):
    """A function that reads from a file."""
    with open(filename, encoding="utf-8") as my_file:
        print(my_file.read())
