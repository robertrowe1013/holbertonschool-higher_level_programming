#!/usr/bin/python3
"""same class of inherited from"""


def is_kind_of_class(obj, a_class):
    """same class or inherited from"""
    if isinstance(obj, a_class):
        return True
    return False
