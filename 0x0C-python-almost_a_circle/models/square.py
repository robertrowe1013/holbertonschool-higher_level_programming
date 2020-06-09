#!/usr/bin/python3
"""square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """squares are rectangles"""

    def __init__(self, size, x=0, y=0, id=None):
        """inherit from rectangle, height and width are size"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.int_validator("width", value)
        self.gtz_validator("width", value)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updater"""
        if kwargs is not None:
            for key, value in kwargs.items():
                update_kwargs = kwargs.copy()
                if key == "size":
                    update_kwargs["width"] = kwargs["size"]
                    update_kwargs["height"] = kwargs["size"]
                super().update(**update_kwargs)
