#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        if not(isinstance(value, int)):
            raise Exception("Exception: Unknown format code 'd' \
for object of type 'str'\n")
        else:
            print("{:d}".format(value))
            return (True)
    except Exception as e:
        sys.stderr.write(str(e))
        return (False)
