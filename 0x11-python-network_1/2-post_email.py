#!/usr/bin/python3
"""Module documentation"""
import urllib.request
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': 'email'})
    data = data.encode(ascii)
    rqst = urllib.request.Request(url, data)
    with urllib.request.urlopen(rqst) as response:
        print(response.read().decode('utf-8'))
