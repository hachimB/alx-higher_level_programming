#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list = my_list[-1::-1]
    for item in my_list:
        print("{:d}".format(item))