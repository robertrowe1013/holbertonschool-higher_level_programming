#!/usr/bin/python3
"""append file"""


def append_write(filename="", text=""):
    """append file"""
    with open(filename, "a+") as my_file:
        my_file.write(text)
        return len(text)
