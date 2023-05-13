#!/usr/bin/python3
if __name__ = "__main__":
    def print_matrix_integer(matrix=[[]]):
        for x in matrix:
            for i, y in enumerate(x):
                print("{}".format(y), end=' ' if i < len(x) - 1 else '\n')
    if len(matrix[0]) == 0:
        print("")
