#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = 0
    if (len(argv) == 1):
        print("%d arguments." % (len(argv) - 1))
    elif (len(argv) == 2):
        print("%d argument:" % (len(argv) - 1))
        count = 1
        print("%d: %s" % (count, argv[1]))
    else:
        print("%d arguments:" % (len(argv) - 1))
        for item in argv[1:]:
            count = count + 1
            print("%d: %s" % (count, item))
