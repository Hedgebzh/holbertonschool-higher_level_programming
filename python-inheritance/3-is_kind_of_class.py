#!/usr/bin/python3
"""Defines a class checking"""


def is_kind_of_class(obj, a_class):
    """check if object is same class"""

    if isinstance(obj, a_class):
        return True
    return False
