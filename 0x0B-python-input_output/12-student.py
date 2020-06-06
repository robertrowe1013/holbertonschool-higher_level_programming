#!/usr/bin/python3
"""student class"""


class Student:
    """student class"""

    def __init__(self, first_name, last_name, age):
        """instantiate student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """class to json"""
        if type(attrs) != list or attrs is None:
            return self.__dict__
        else:
            attr_dict = {}
            for key in self.__dict__:
                for key2 in attrs:
                    if key == key2:
                        attr_dict[key] = self.__dict__[key]
                return attr_dict
