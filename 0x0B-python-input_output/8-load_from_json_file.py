#!/usr/bin/python3
"""create object from JSON"""


def load_from_json_file(filename):
    """create object from JSON"""
    import json
    with open(filename) as my_file:
        return json.load(my_file)        
