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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                for i2 in range(self.size):
                    print("#", end='')
                print("")
