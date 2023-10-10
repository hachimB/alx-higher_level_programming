#!/usr/bin/python3
"""Module documentation"""


def append_write(filename="", text=""):
    """ function that appends a string at the end
of a text file (UTF8) and returns the number of characters added"""
    with open(filename, "a", encoding="utf8") as file:
        tail = file.tell()
        file.write(text)
        tail_2 = file.tell()
    return (tail_2 - tail)
