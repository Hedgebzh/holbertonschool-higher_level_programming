#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """function for write in a file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
