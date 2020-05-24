#!/usr/bin/python3
"""add int

"""


def add_integer(a, b=98):
    """add int

    """
    try:
        a += 0
    except TypeError:
        raise TypeError("a must be an integer")
    try:
        b += 0
    except TypeError:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
