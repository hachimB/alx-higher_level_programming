#!/usr/bin/python3
for number in range(0, 100):
    if (number < 10):
        output = "0{}, ".format(number)
    elif (number < 99):
        output = "{}, ".format(number)
    else:
        output = number
    print(output, end='')
print()
