#!/usr/bin/python3
"""print file"""


def read_file(filename=""):
    """print file"""
    with open(filename, encoding="UTF*") as my_file:
        print(my_file.read())
