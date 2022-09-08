#!/usr/bin/python3
def uppercase(str):
    result = ''
    for index in str:
        if ord(index) >= 97 and ord(index) < 123:
            result += chr(ord(index) - 32)
        else:
            result += index
    print(f'{result}')
