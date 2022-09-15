#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    , 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    roman_to_int = 0

    for i in range(len(roman_string)):
        roman_to_int += roman_int[roman_string[i]]
    return (roman_to_int)
