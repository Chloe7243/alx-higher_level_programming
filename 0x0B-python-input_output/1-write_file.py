#!/usr/bin/python3
""" writes to file and returns the number of characters written """


def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        characters = f.write(text)
        return characters

nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)
