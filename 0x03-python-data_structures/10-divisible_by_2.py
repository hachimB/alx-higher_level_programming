#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = []
    l = len(my_list)
    for i in range(l):
        if (my_list[i] % 2 == 0):
            list.append(True)
        else:
            list.append(False)
    return (list)
