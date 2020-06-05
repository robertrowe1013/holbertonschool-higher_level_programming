#!/usr/bin/python3
"""read n lines"""


def read_lines(filename="", nb_lines=0):
    """read n lines"""
    with open(filename) as my_file:
        if nb_lines < 1:
            print(my_file.read(), end='')
        else:
            for i in range(nb_lines):
                print(my_file.readline(), end='')
                i += 1
