#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    index = 1
    count = len(sys.argv) - 1
    if count == 0:
        print('0 arguments')
    elif count == 1:
        print('{} argument'.format(count), end="\n")
    else:
        print('{} arguments'.format(count), end="\n")
    for index in range(count):
        print('{}: {}'.format(index, sys.argv[index + 1]), end="\n")
