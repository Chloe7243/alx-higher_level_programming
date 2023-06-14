#!/usr/bin/python3
""" appends to text and returns the number of characters written """


def append_write(filename="", text=""):
    with open(filename, "a") as f:
        return f.write(text)
