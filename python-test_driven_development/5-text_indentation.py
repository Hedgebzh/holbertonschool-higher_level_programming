#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """Text indentation function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        print("{}".format(text[i]), end="")
        if text[i] == "." or text[i] == "," or text[i] == "?":
            print("\n")
