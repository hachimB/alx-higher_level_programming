#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (idx < 0):
        list = my_list
    elif (idx > len(my_list) - 1):
        list = my_list
    else:
        my_list[idx] = element
        list = my_list
    return (list)
