#!/usr/bin/python3
"""Defines a square.

"""


class Square:
    """A plane figure with four equal length sides and four right angles.

    """
    def __init__(self, size=0, position=(0, 0)):
        """length of size.

        """
        self.__size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[1] < 0 or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return (self.__size ** 2)

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            print("\n" * self.position[1], end='')
            for i in range(self.size):
                print(" " * self.position[0], end='')
                print("#" * self.size, end='')
                print("")

    def __str__(self):
        sq = ""
        if self.size == 0:
            return sq
        else:
            for pos in range(self.position[1]):
                sq += "\n"
            for i in range(self.size):
                for i2 in range(self.position[0]):
                    sq += " "
                for i3 in range(self.size):
                    sq += "#"
                if i + 1 != self.size:
                    sq += "\n"
        return sq
