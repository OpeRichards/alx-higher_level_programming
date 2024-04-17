#!/usr/bin/python3
"""A module for a function pascal_triangle."""


def pascal_triangle(n):
    """A function that defines a Pascal's Triangle of size n.
    Args:
        n (int): Size of Pascal's triangle.
    Returns:
        list of lists: list of lists of integers representing
        the Pascal’s triangle of size n.
        empty list: if n <= 0
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles