#!/usr/bin/python3
"""This module creates a class MyList."""


class MyList(list):
    
    def print_sorted(self):
        print(sorted(self))
