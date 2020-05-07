#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqrlist = []
    for i in matrix:
        sqrlist.append(list(map(lambda x: x**2, i)))
    return sqrlist
