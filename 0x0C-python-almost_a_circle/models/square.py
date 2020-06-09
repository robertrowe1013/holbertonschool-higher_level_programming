#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """squares are rectangles"""
    def __init__(self, size, x=0, y=0, id=None):
        """inherit from rectangle, height and width are size"""
        super().__init__(height=size, width=size, x=x, y=y, id=id)
