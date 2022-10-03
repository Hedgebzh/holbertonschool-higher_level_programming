#!/usr/bin/python3
"""Rectangle module for almost a circle"""
from models.base import Base

class Rectangle(Base):
    """Represent a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

    @property
    def size(self):
        return(self.__size)

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return(self.__x)

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return(self.__y)

    @y.setter
    def y(self, value):
        self.__y = value

