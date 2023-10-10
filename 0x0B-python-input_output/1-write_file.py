#!/usr/bin/python3
"""Module documentation"""


def write_file(filename="", text=""):
    """function that writes a string to a text
file (UTF8) and returns the number of characters written"""
    with open(filename, "w", encoding="utf8") as file:
        file.write(text)
        tail = file.tell()
    return (tail)
