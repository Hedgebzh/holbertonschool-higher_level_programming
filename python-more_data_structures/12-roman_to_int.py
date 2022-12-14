#!/usr/bin/python3
def roman_to_int(roman_string):
    romdic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = 0
    if roman_string is None or isinstance(roman_string, str) is False:
        return (0)
    for i in range(len(roman_string)):
        if i > 0 and romdic[roman_string[i]] > romdic[roman_string[i - 1]]:
            r += romdic[roman_string[i]]
        else:
            r += romdic[roman_string[i]]
    return (r)
