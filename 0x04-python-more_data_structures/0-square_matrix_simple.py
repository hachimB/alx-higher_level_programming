#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for item in matrix:
        matrix_2 = map(lambda item: [i * i for i in item], matrix)
    return (list(matrix_2))
