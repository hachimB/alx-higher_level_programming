#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for keys in a_dictionary:
        if key not in a_dictionary:
            return (a_dictionary)
        else:
            del a_dictionary[key]
            return (a_dictionary)
