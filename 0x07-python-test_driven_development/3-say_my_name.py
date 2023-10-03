#!/usr /bin/python3
"""Module documentation
second line
third line
forth line
"""


def say_my_name(first_name, last_name=""):
    """ say_my_name function
raises TypeError when failed
"""
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
