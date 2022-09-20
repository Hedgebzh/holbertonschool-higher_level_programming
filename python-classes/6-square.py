#!/usr/bin/python3
'''module documentation'''


from turtle import position


class Square:
    '''Class named square'''
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position=(0, 0)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        area = self.__size**2
        return (area)

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for y in range(self.__size):
                print("#", end="")
            print("")
