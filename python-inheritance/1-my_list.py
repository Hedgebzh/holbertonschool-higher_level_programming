#!/usr/bin/python3
'''my list class'''


class MyList(list):
    def print_sorted(self):
        """print_sorted function"""
        print(sorted(self))
