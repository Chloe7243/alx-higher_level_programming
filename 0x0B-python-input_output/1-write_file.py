#!/usr/bin/python3
""" writes to file and returns the number of characters written """


def write_file(filename="", text=""):
    """
        function receives a filename and a text
        then writes the text into the file with the file name
        returning the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as fl:
        return fl.write(text)
