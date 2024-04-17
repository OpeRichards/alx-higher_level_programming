#!/usr/bin/python3
"""This module defines class Student."""


class Student:
    """A class Student that defines a student data."""
    def __init__(self, first_name, last_name, age):
        """Initializes class Student.
        Args:
            first_name (str): First name of a student.
            last_name (str): Last name of a student.
            age (int): Age of a student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a student"""
        return self.__dict__

    def to_json(self, attrs=None):
        """Return a class Student to JSON with filter.
        If a list of strings exist, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and \
                all(type(ele) == str for ele in attrs)):
                    return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
            return self.__dict__
