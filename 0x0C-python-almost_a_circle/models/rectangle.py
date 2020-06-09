#!/usr/bin/python3
"""rectangle class"""
from models.base import Base


class Rectangle(Base):
    """retangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self.int_validator("width", value)
        self.gtz_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        self.int_validator("height", value)
        self.gtz_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        self.int_validator("x", value)
        self.goet_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        self.int_validator("y", value)
        self.goet_validator("y", value)
        self.__y = value

    def area(self):
        """area func"""
        return self.__width * self.__height

    def display(self):
        """print rectangle"""
        print_string = ""
        for i in range(self.y):
            print_string += "\n"
        for i2 in range(self.height):
            for i3 in range(self.x):
                print_string += " "
            for i4 in range(self.width):
                print_string += "#"
            print_string += "\n"
        print(print_string, end='')

    def __str__(self):
        """str override"""
        if self.__class__.__name__ == "Rectangle":
            return ("[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
                self.__class__.__name__, self.id, self.__x,
                self.__y, self.__width, self.__height))
        elif self.__class__.__name__ == "Square":
            return ("[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
                self.__class__.__name__, self.id, self.__x,
                self.__y, self.__width))

    def update(self, *args, **kwargs):
        """updater"""
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    super().__init__(value)
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
        if len(args) >= 1:
            super().__init__(args[0])
        if len(args) >= 2:
            self.__width = args[1]
        if len(args) >= 3:
            self.__height = args[2]
        if len(args) >= 4:
            self.__x = args[3]
        if len(args) == 5:
            self.__y = args[4]
