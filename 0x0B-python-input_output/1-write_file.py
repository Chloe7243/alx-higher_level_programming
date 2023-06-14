#!/usr/bin/python3
""" writes to file and returns the number of characters written """


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
