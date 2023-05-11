#!/usr/bin/python3
def uppercase(str):
    ustr = ""
    for c in str:
        if 97 <= ord(c) and 122 >= ord(c):
            ustr += chr(ord(c) - 32)
        else:
            ustr += c
    print("{}".format(ustr))
