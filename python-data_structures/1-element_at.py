#!/usr/bin/python3
from socket import if_nameindex


def element_at(my_list, idx):
    if idx < 0:
        return None
    if idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
