#!/usr/bin/python3
"""new class named Basegeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """new class inherits of Basegeometry"""
    def __init__(self, width, height):
        """initialize a new rectangle"""
        self.integer_validator("width", width)
        self.width = width
        self.integer_validator("height", height)
        self.height = height
