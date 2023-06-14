#!/usr/bin/python3
""" writes to file and returns the number of characters written """


def write_file(filename="", text=""):
    with open(filename, "w") as f:
        return f.write(text)
