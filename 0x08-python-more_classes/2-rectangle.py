#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Plane figure with four sides and four right angles"""
    def __init__(self, width=0, height=0):
        """Instantiation"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height muxt be >= 0")

    def area(self):
        """area of a rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """perimeter of a rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return ((self.height + self.width) * 2)
