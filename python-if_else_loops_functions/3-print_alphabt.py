#!/usr/bin/python3
alphabet = ""
for idx in range(97, 123):
    if chr(idx) != 'q' and chr(idx) != 'e':
        print('{}'.format(chr(idx)), end="")
