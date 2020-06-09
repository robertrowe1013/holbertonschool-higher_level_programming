#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """squares are rectangles"""
    def __init__(self, size, x=0, y=0, id=None):
        """inherit from rectangle, height and width are size"""
        super().__init__(height=size, width=size, x=x, y=y, id=id)
        self.size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter"""   
        self.int_validator("width", value)
        self.gtz_validator("width", value)
        self.width = value
        self.height = value
        self.__size = value
