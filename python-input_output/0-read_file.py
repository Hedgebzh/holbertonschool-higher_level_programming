#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """function for read a file in python"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
