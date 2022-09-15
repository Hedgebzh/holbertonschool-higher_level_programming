#!/usr/bin/python3
import string


def roman_to_int(roman_string):
    romdic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = 0
    if roman_string is None or roman_string is not string:
        return (0)
    for i in range(len(roman_string)):
        if i > 0 and romdic[roman_string[i]] > romdic[roman_string[i - 1]]:
                r += romdic[roman_string[i]] - 2 * romdic[roman_string[i - 1]]
        else:
            r += romdic[roman_string[i]]
    return (r)
