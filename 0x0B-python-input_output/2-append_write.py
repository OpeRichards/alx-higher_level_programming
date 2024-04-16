#!/usr/bin/python3
"""This defines a function append_write."""


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as my_file:
        return my_file.write(text)
