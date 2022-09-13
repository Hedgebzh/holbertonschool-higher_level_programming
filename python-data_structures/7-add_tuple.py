#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    #tuple_add = tuple(i + j for i in tuple_a for j in tuple_b)
    #return(tuple_add)

    if len(tuple_a) or len(tuple_b) < 2:
        for i in tuple_a:
            if i == "":
                i = 0
        for j in tuple_b:
            if i == "":
                j = 0


    new_tuple = tuple(map(lambda x, y: x + y, tuple_a, tuple_b))
    return(new_tuple)
