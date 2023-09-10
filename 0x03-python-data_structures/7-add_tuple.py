#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    if (len(tuple_a) < 2):
        if (len(tuple_a) == 1):
            tuple_a.append(0)
        else:
            tuple_a.append(0)
            tuple_a.append(0)
    elif (len(tuple_b) < 2):
        if (len(tuple_b) == 1):
            tuple_b.append(0)
        else:
            tuple_b.append(0)
            tuple_b.append(0)
    tuple_a = tuple(tuple_a)
    tuple_b = tuple(tuple_b)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (new_tuple)
