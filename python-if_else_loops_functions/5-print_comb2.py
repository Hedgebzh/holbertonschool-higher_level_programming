#!/usr/bin/python3
hexadecimal = ''
for idx in range(0, 99):
    if idx < 10:
        print('0{}'.format(idx), end="\n")
    if idx > 9:
        print('{}'.format(idx), end="\n")
