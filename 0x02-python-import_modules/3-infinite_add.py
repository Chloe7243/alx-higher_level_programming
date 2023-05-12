#!/usr/bin/python3

from sys import argv
args = argv[1:]
result = 0
for arg in args:
    result += int(arg)
print(result)
