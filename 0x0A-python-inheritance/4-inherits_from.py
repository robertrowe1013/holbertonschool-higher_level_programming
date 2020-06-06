#!/usr/bin/python3
"""only subclass"""


def inherits_from(obj, a_class):
    """only subclass"""
    if issubclass(obj.__class__, a_class) is True and type(obj) is not a_class:
        return True
    return False
