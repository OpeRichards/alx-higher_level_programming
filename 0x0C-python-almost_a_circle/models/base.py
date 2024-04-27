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

    @classmethod
    def save_to_file(cls, list_objs):
        """Method writes the JSON string representation of list_objs to a file.
        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.
        Args:
            json_string: a string representing a list of dictionaries
        Returns:
            the list represented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
