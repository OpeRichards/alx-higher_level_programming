#!/usr/bin/python3
"""This defines a function ``matrix_divided``."""


def matrix_divided(matrix, div):
    """Function ``matrix_divided`` divides all elements
    of a matrix with a divisor.
    Args:
        matrix (list): A list of lists with same size, and
                        with final elements are integers.
        div (int): Integer to divide matrix
    Returns:
        A new matrix: Result of the divisions.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and
               all(isinstance(elem, (int, float))
                   for elem in row) for row in matrix):
        # If not, raise a TypeError
        raise TypeError(
            'matrix must be a matrix (list of lists)'
            ' of integers/floats')

    # Check if each matrix is of same size
    rows = len(matrix[0])
    # Iterate through the matrix starting from the second one
    for remLists in matrix[1:]:
        # Check if the dimensions match
        if len(remLists) != rows:
            raise TypeError('Each row of the matrix must have the same size')

    # Check if div is a number: int or float
    if not isinstance(div, (int, float)):
        # If not, raise TypeError
        raise TypeError('div must be a number')

    # Check if div not equal to 0
    if div == 0:
        # if true, raise ZeroDivisionError
        raise ZeroDivisionError('division by zero')

    # Divide each element of the matrix by div and
    # round the result to 2 significant figures
    result = [[round(elem / div, 2) for elem in row] for row in matrix]
    return result
