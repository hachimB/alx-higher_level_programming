#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    """if (len(tuple_a) < 2):
        if (len(tuple_a) == 1):
            if (tuple_a[0] is None):
                tuple_a[0] = 0
                tuple_a.append(0)
            tuple_a.append(0)
        else:
            tuple_a.append(0)
            tuple_a.append(0)
    elif (len(tuple_b) < 2):
        if (len(tuple_b) == 1):
            if (tuple_b[0] is None):
                tuple_b[0] = 0
                tuple_b.append(0)
            tuple_b.append(0)
        else:
            tuple_b.append(0)
            tuple_b.append(0)
    tuple_a = tuple(tuple_a)
    tuple_b = tuple(tuple_b)"""
    for i in range(2):
        if len(tuple_a) <= i or tuple_a[i] is None:
            tuple_a.append(0)

        if len(tuple_b) <= i or tuple_b[i] is None:
            tuple_b.append(0)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (new_tuple)
