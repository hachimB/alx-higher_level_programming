#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for c in my_list:
            count += 1
        '''if (x > count):
            count = x
            IndexError'''
        count = 0
        for i in my_list[:x]:
            if (type(i) == int):
                count += 1
                print("{:d}".format(i), end="")
        print()
        return (count)
    except IndexError as e:
        print(e)
"""def safe_print_list_integers(my_list=[], x=0):
    try:
        list2 = []
        count = 0
        c = 0
        for e in my_list:
            count += 1
        if (x > count):
            raise IndexError
        count = 0
        for i in my_list:
            if (type(i) == int):
                list2.append(i)
        for i in list2:
            c += 1
        for l in list2:
            count += 1
            print("{:d}".format(l), end="")
        print()
        return (c)
    except IndexError as e:
        print (e)"""
