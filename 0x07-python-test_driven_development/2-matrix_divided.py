#!/usr/bin/python3
"""divide a matrix"""


def matrix_divided(matrix, div):
    """divide a matrix"""
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    for row in range(len(matrix) - 1):
        if len(matrix[row]) != len(matrix[row + 1]):
                raise TypeError("Each row of the matrix "
                                "must have the same size")
    new_matrix = []
    for row in matrix:
        for i in row:
            try:
                new_matrix.append([round(i / div, 2)])
            except ZeroDivisionError:
                raise ZeroDivisionError("division by zero")
            except TypeError:
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
    return new_matrix
