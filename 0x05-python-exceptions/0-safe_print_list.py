#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for c in my_list:
            count += 1
        if (x > count):
            x = count
        for i in my_list[:x]:
            print(i, end="")
        print()
        return (x)
    except Exception as e:
        print(e)
