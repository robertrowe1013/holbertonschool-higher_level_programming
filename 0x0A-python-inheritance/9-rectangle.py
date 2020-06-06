#!/usr/bin/python3
"""rectangle class"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """retangle class"""
    def __init__(self, width, height):
        """init rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """area"""
        return (self.__width * self.__height)

    def __repr__(self):
        """print format"""
        return "[{:s}] {:d}/{:d}".format(self.__class__.__name__, self.__width, self.__height)
