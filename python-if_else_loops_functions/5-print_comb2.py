#!/usr/bin/python3

for idx in range(0, 100):
    if idx < 99:
        print('{:02}'.format(idx), end=", ")
    if idx == 99:
        print('{}'.format(idx))
