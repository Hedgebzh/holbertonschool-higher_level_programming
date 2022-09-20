#!/usr/bin/python3
#!/usr/bin/python3
'''module documentation'''


class Square:
    '''Class named square'''
    def __init__(self, size=0):
        self.__size = size
        if size == isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
