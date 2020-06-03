#!/usr/bin/python3
"""count lines"""


def number_of_lines(filename=""):
    """count lines"""
    with open(filename, encoding="UTF*") as my_file:
        file_count = len(my_file.readlines())
        return file_count
