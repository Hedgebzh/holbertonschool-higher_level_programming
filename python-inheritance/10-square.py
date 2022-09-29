#!/usr/bin/python3
"""new class named square"""
Rectangle = __import__('9-rectangle.py').Rectangle

class Square:
    """new class named square"""
    def __init__(self, size):
        self.size = size
        self.integer_validator("size", size)
