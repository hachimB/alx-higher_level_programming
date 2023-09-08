#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for chars in my_string:
        if (chars != chr(67) and chars != chr(99)):
            new_str = new_str + chars
    return(new_str)
