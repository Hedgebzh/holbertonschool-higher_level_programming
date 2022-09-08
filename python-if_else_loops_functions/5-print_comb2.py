#!/usr/bin/python3
hexadecimal = ''
for idx in range(0, 100):
    if idx < 10:
        print('0{}, '.format(idx), end="")
    if idx < 99:
        print('{}, '.format(idx), end="")
    else:
        print('{}'.format(idx), end="\n")
