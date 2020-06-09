#!/usr/bin/python3
"""base class"""
import json


class Base:
    """base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def int_validator(self, name, value):
        """int validator"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))

    def gtz_validator(self, name, value):
        """greater than zero error"""
        if value < 1:
            raise ValueError("{:s} must be > 0".format(name))

    def goet_validator(self, name, value):
        """greater than or equal to error"""
        if value < 0:
            raise ValueError("{:s} must be >= 0".format(name))

    def to_json_string(list_dictionaries):
        """dict to JSON"""
        return json.dumps(list_dictionaries)
