#!/usr/bin/python3
"""Module documentation"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, "r", encoding="utf8") as file:
        content = file.read()
        print(content, end='')
