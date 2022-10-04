#!/usr/bin/python3
"""Rectangle module for almost a circle"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize with defaults attribute the object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Function for calculate area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Function for print the rectangle with #"""
        for i in range(self.__y):
            print("")
        for j in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for x in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "] " + "("
        string += str(self.id) + ") " + str(self.__x) + "/" + str(self.__y)
        string += " - " + str(self.__width) + "/" + str(self.__height)
        return (string)

    def update(self, *args):
        """Update function for define new attributes"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1
