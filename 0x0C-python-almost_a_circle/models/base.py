#!/usr/bin/python3
"""This defines a class ``Base``."""

import json


class Base:
    """Initialize a class Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of ``list_dictionaries``.
        Args:
            list_dictionaries (list): A list of dictionaries.
        Returns:
            "[]": if None or empty
            JSON string representation: if not None or not empty
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
