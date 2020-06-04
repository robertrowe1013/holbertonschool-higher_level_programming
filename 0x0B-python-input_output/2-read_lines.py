#!/usr/bin/python3
"""read n lines"""


def read_lines(filename="", nb_lines=0):
    "read n lines"
    with open(filename, encoding="UTF8") as my_file:
        if nb_lines < 1:
            print(my_file.read())
        elif nb_lines > len(my_file.readlines()):
            print(my_file.read())
        else:
            
