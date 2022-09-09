#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    add_result = 0
    n = len(sys.argv)
    for index in range(1, n):
        add_result += int(sys.argv[index])
    print('{}'.format(add_result), end="\n")
