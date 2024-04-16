#!/usr/bin/python3
"""This is a function to_json_string."""


import json
"""Import JSON module"""


def from_json_string(my_str):
    """A function that to decode or return an
    object represented by a string object.
    Returns:
        json : The file as a string object.
    """
    return json.loads(my_str)
