#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    rev_list = my_list[::-1]
    i = 0
    while i < len(rev_list):
        print("{:d}".format(rev_list[i]))
        i += 1
