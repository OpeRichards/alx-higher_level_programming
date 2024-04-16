#!/usr/bin/python3
"""This defines a function write_file."""


def write_file(filename="", text=""):
    """This function writes into a file.
    Args:
        filename: A file to read from and write into.
        text: The new string to write into the file filename.
    """
    with open(filename, mode="w", encoding="utf-8") as my_file:
        return my_file.write(text)
