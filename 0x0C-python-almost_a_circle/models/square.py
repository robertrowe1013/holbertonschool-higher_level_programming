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
        if len(args) > 0:
            update_args = []
            update_args.append(args[0])
            if len(args) > 1:
                update_args.append(args[1])
                for i in range(1, len(args)):
                    update_args.append(args[i])
            super().update(*update_args)
        elif kwargs is not None:
            for key, value in kwargs.items():
                update_kwargs = kwargs.copy()
                if key == "size":
                    update_kwargs["width"] = kwargs["size"]
                    update_kwargs["height"] = kwargs["size"]
                super().update(**update_kwargs)

    def to_dictionary(self):
        """square dictionary"""
        return ({"id": self.id, "size": self.size, "x": self.x, "y": self.y})
