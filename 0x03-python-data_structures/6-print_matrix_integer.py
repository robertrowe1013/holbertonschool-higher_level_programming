#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        for element in row:
            if element == row[0]:
                print("{:d}".format(element), end='')
            else:
                print(" {:d}".format(element), end='')
        print()
