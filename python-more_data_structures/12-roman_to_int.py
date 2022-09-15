#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,'M': 1000}
    roman_to_int = 0

    for i in range(len(roman_string)):
        if i > 0 and rom_int[roman_string[i]] > rom_int[roman_string[i - 1]]:
                roman_to_int += rom_int[roman_string[i]] - 2 * rom_int[roman_string[i - 1]]
        else:
            roman_to_int += rom_int[roman_string[i]]
    return (roman_to_int)
