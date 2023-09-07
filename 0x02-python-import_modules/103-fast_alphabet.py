#!/usr/bin/python3
from sys import stdout
stdout.buffer.write(bytes(range(ord('A'), ord('Z')+1)) + b'\n')
