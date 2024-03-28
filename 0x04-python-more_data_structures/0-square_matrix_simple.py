#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for elem in matrix:
        new_row = []
        for x in elem:
            new_row.append(x**2)
        new_matrix.append(new_row)
    return new_matrix
