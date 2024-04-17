#!/usr/bin/python3
"""This is a function save_to_json_string."""


import json
"""Import JSON module"""


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a
    text file, using a JSON representation.
    Args:
        my_obj: JSON file.
        filename: File to write into.
    Returns:
        json : The file as a string object.
    """
    with open(filename, mode='w', encoding='utf-8') as my_file:
        json.dump(my_obj, my_file)
