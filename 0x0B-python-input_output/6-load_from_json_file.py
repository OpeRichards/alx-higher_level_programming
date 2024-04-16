#!/usr/bin/python3
"""This is a function load_from_json_file."""


import json
"""Import JSON module"""


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”.
    Args:
        filename: File to write from.
    Returns:
        new_file : The Object file created from filename.
    """
    with open(filename, mode='r', encoding='utf-8') as new_file:
        return json.load(new_file)