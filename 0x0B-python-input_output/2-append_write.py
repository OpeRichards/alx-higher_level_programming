#!/usr/bin/python3
"""This defines a function append_write."""


def append_write(filename="", text=""):
    """This function appends to a file.
    Args:
        filename: File to append into.
        text: The new string to append into the file filename.
    """
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
