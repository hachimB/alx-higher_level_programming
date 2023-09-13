#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys in a_dictionary:
        if key in a_dictionary:
            del a_dictionary[key]
        else:
            a_dictionary = a_dictionary
        return (a_dictionary)
