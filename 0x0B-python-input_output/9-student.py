#!/usr/bin/python3
"""This module defines class Student."""


class Student:
    """A class Student that defines a student data.
    Args:
        first_name (str): First name of a student.
        last_name (str): Last name of a student.
        age (int): Age of a student.
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
