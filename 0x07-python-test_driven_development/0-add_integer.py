#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        a += 0
    except TypeError:
        raise TypeError("a must be an integer")
    try:
        b += 0
    except TypeError:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
