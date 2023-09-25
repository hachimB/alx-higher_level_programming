#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for c in my_list:
            count += 1
        count = 0
        for i in my_list[:x]:
            if (type(i) == int):
                count += 1
                print("{:d}".format(i), end="")
        print()
        return (count)
    except IndexError as e:
        print(e)
