#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first_c = None
    if (length > 0):
        first_c = sentence[0]
    tuple = (length, first_c)
    return (tuple)
