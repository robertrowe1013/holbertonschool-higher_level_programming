#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Plane figure with four sides and four right angles"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation"""
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        self.id = Rectangle.number_of_instances

    def __del__(self):
        """delete with message"""
        del self
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def __str__(self):
        """save as string"""
        rec = ""
        if self.area == 0:
            return rec
        else:
            for i in range(self.height):
                for i2 in range(self.width):
                    rec += str(self.print_symbol)
                if i + 1 != self.height:
                    rec += "\n"
        return rec

    def __repr__(self):
        """save as string"""
        rec = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return rec

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """compares area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return (rect_2)
        else:
            return (rect_1)

    @classmethod
    def square(cls, size=0):
        """squares are rectangles"""
        return Rectangle(size, size)
