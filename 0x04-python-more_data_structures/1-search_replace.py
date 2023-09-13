#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if (my_list is None or search is None or replace is None):
        return
    new_list = [num for num in my_list]
    for i in range(len(new_list) - 1):
        if (new_list[i] == search):
            new_list[i] = replace
    return (new_list)
