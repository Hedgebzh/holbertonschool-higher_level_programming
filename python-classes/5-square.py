#!/usr/bin/python3
'''module documentation'''


class Square:
    '''Class named square'''
    def __init__(self, size=0):
        self.__size = size

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

    def area(self):
        area = self.__size**2
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print("\n", end="")
        for i in range(self.size):
            for i in range(self.size):
                print("#", end="")
            print("")

