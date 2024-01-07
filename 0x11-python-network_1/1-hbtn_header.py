#!/usr/bin/python3
"""Module documentation"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header_variable = response.getheader('X-Request-Id')
    print(header_variable)
