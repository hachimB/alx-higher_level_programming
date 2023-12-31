#!/usr/bin/python3
"""module doc
second line
third line
forth line
"""


def matrix_divided(matrix, div):
    """matrix_divided function
raises some errors when failed
"""
    if not matrix or not isinstance(matrix[0], list):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    length = len(matrix[0])
    mtx = []
    if not (isinstance(div, (int, float))):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    for items in matrix:
        for i in items:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)\
of integers/floats")
        if not (length == len(items)):
            raise TypeError("Each row of the matrix must have the same size")
        row = [round(i / div, 2) for i in items]
        mtx.append(row)
    return (mtx)
