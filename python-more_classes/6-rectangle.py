#!/usr/bin/python3
"""Rectangle class module"""


class Rectangle:
    """Class named rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return(self.__height * self.__width)

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return (0)
        return((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectangle = []
        for i in range(self.__height):
            for j in range(self.__width):
                rectangle.append("#")
            rectangle.append("\n")
        return ("".join(rectangle))[:-1]

    def __repr__(self): # récrée littéralement l'objet ?
        new_rectangle = "Rectangle (" + str(self.width)
        new_rectangle += "," + str(self.height) + ")"
        return (new_rectangle)

    def __del__(self):
        print("Bye rectangle...")
