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
        self.__width = value
        self.__height = value
        self.__size = value

    def update(self, *args, **kwargs):
        """updater"""
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(height=self.size,
                                     width=self.size, id=value)
                if key == "size":
                    self.__size = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
        if len(args) >= 1:
            super().__init__(width=self.size, height=self.size, id=args[0])
        if len(args) >= 2:
            self.__size = args[1]
        if len(args) >= 3:
            self.__x = args[2]
        if len(args) == 4:
            self.__y = args[3]
