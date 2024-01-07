#!/usr/bin/python3
"""Module documentation"""


def find_peak(list_of_integers):
    """find_peak function"""
    if list_of_integers:
        peak = list_of_integers[0]
        for number in list_of_integers:
            if number > peak:
                peak = number
        return peak
    else:
        return None
