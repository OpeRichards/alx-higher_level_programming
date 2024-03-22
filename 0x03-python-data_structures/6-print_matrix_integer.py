#!/bin/usr/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for index, x2 in enumerate(x):
            if index == len(x) - 1:
                print('{:d}'.format(x2), end='')
            else:
                print('{:d}'.format(x2), end=' ')
        print()
