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

    @staticmethod
    def to_json_string(list_dictionaries):
        """dict to JSON"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """str to dict"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """json string to file"""
        list_dict = []
        if list_objs is None:
            list_objs = []
        for obj in list_objs:
            list_dict.append(obj.to_dictionary())
        json_string = cls.to_json_string(list_dict)
        filename = "{:s}.json".format(cls.__name__)
        with open(filename, 'w+') as my_file:
            my_file.write(json_string)
