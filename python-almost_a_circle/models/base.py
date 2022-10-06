#!/usr/bin/python3
"""Base module for almost a circle"""


import json


class Base:
    """Base class for almost a circle"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Init function of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Format for sharing data representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return("[]")
        return json.dumps(list_dictionaries)
