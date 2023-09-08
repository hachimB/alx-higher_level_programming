#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list = [item for item in my_list]
    if (idx < 0):
        return (list)
    elif (idx > len(my_list) - 1):
        return (list)
    else:
        list[idx] = element
        return (list)
