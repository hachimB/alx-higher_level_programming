#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary)
    for keys in sorted_keys:
        print("{:s}: {}".format(keys, a_dictionary[keys]))
