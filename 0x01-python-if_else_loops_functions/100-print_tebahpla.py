#!/usr/bin/python3
for num in range(122, 96, -1):
    if (num % 2 != 0):
        num = num - 32
    ch = chr(num)
    print("{}".format(ch), end='')
