#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = list(tuple_a)
    tuple_b = list(tuple_b)
    for i in range(2):
        if len(tuple_a) <= i or tuple_a[i] is None:
            tuple_a.append(0)

        if len(tuple_b) <= i or tuple_b[i] is None:
            tuple_b.append(0)
    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return (new_tuple)
