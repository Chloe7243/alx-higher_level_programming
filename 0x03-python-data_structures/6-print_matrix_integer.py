#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for i, y in enumerate(x):
            print("{:d}".format(y), end=' ' if i < len(x) - 1 else '\n')
    if len(matrix[0]) == 0:
        print("")
