#!/usr/bin/python3
"""base geometry class"""


class BaseGeometry:
    """base geometry class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("name must be an integer")
        if value < 1:
            raise ValueError("name must be greater than 0")
