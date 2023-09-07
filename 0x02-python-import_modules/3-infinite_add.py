#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    if (len(argv) == 1):
        print("%d" % (len(argv) - 1))
    else:
        for item in argv[1:]:
            item = int(item)
            result = result + item
        print("%d" % (result))
