#!/usr/bin/python3
"""inherit print sorted"""


class MyList(list):
    """inherit print sorted"""
    def print_sorted(self):
        sortedlist = sorted(self)
        print(sortedlist)
