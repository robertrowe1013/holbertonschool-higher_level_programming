#!/usr/bin/python3
"""square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """squares are rectangles"""
    def __init__(self, size):
        """init square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
