#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        list2 = []
        for c in my_list:
            count += 1
        if (x > count):
            for i in my_list:
                print(i, end="")
            print()
        else:
            for i in my_list:
                list2 = my_list[:x]
            for i in list2:
                print(i, end="")
            print()
        return (i)
    except Exception as e:
        print(e)
