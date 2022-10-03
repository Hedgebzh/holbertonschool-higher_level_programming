#!/usr/bin/python3
"""Base module for almost a circle"""


class Base:
    """Base class for almost a circle"""
    __nb_objects = 0
    def __init__(self, id=None):
        """Init function of the class"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
