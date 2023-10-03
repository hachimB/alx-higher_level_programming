#!/usr/bin/python3
"""module doc
second line
third line
forth line
"""


def text_indentation(text):
    """test_indentation
raise some errors when failed
"""
    if not (isinstance(text, str)):
        raise TypeError("text must be a string")
    for i in text:
        if i == "." or i == "?" or i == ":":
            print(i)
            print()
        else:
            print(i, end="")
