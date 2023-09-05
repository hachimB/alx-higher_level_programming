#!/usr/bin/python3
def uppercase(str):
    for s in str:
        if (ord(s) >= 97 and ord(s) < 123):
            up = ord(s) - 32
            s = chr(up)
        print("{}".format(s), end='')
    print()
