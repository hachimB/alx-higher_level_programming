#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_c = sentence[0]
    if (length == 0):
        first_c = None
    tuple = (length, first_c)
    return (tuple)
