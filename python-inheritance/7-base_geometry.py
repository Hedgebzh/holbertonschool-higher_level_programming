#!/usr/bin/python3
"""new class named Basegeometry"""


class BaseGeometry:
    """new class named BaseGeometry"""
    def area(self):
        """not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
