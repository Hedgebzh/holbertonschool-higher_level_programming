#!/usr/bin/python3
'''my list class'''


class MyList(list):
    """new class named MyList"""
    def print_sorted(self):
        """print_sorted function"""
        print(sorted(self))
