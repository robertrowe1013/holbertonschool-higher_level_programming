#!/usr/bin/python3
"""print square"""


def print_square(size):
    """print square"""
    try:
        size += 0
    except TypeError:
        raise TypeError("size must be an integer")
    if (type(size) == float) & (size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for i2 in range(size):
            print("#", end='')
        print("")
