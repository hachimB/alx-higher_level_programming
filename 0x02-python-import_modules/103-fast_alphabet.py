#!/usr/bin/python3
#from string import ascii_uppercase
#exec("from sys import stdout; stdout.write(ascii_uppercase + '\\n')")
from sys import stdout
stdout.buffer.write(bytes(range(ord('A'), ord('Z')+1)) + b'\n')
