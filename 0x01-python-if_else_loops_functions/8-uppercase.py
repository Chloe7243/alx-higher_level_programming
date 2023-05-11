#!/usr/bin/python3
def uppercase(str):
    for i, c in enumerate(str):
        if 97 <= ord(c) and 122 >= ord(c):
            print(chr(ord(c) - 32), end='' if len(str) - 1 != i else "\n")
        else:
            print(c, end='' if len(str) - 1 != i else "\n")
