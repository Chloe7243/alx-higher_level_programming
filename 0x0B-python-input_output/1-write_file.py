#!/usr/bin/python3
""" writes to file and returns the number of characters written """


def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        characters = f.write(text)
        f.close()
        return characters
