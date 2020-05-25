#!/usr/bin/python3
"""divide a matrix"""


def matrix_divided(matrix, div):
    """divide a matrix"""
    new_matrix = matrix.copy()
    for row in range(len(new_matrix) - 1):
        if len(new_matrix[row]) != len(new_matrix[row + 1]):
                raise TypeError("Each row of the matrix "
                                "must have the same size")
    for i in range(len(new_matrix)):
        for i2 in range(len(new_matrix[i])):
            try:
                new_matrix[i][i2] = round((new_matrix[i][i2] / div), 2)
            except ZeroDivisionError:
                raise ZeroDivisionError("division by zero")
            except TypeError:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return new_matrix
