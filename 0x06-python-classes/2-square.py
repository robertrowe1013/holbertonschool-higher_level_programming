#!/usr/bin/python3
"""Defines a square.

"""


class Square:
    """A plane figure with four equal length sides and four right angles.

    """
    def __init__(self, size=0):
        """length of size.

        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
