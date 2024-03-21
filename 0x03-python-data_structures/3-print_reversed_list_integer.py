#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for num in reverse(my_list):
        if not num < 0 or num >= len(my_list):
            print('{:d}'.format(num))
