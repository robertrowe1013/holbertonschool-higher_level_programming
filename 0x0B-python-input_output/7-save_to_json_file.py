#!/usr/bin/python3
"""wrtie object with json"""


def save_to_json_file(my_obj, filename):
    """write object with json"""
    import json
    with open(filename, "w") as my_file:
        my_file.write(json.dumps(my_obj)
