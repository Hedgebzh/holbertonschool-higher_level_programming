#!/usr/bin/python3
"""Defines a class checking"""


def inherits_from(obj, a_class):
    """check if object is same class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
