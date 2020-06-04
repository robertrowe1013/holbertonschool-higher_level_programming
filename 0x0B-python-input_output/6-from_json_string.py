#!/usr/bin/python3
"""from JSON string"""


def from_json_string(my_str):
    """from json to string"""
    import json
    return json.loads(my_str)
