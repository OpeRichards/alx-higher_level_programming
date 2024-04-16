#!/usr/bin/python3
"""This is a function to_json_string."""


import json
"""Import JSON module"""


def to_json_string(my_obj):
    """A function that to view the JSON
    representation of a string object.
    Returns:
        json : The file as a string object.
    """
    return json.dumps(my_obj)
