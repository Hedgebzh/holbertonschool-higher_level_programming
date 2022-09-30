#!/usr/bin/python3
"""append write module"""


def append_write(filename="", text=""):
    """function for append write in a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
