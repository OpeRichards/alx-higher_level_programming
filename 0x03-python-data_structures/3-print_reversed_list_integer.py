#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for num in my_list:
        if not num == '':
            print('{:d}'.format(num))
