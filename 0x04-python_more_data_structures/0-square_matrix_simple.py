#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        return matrix
    new_matrix = []
    for i, x in enumerate(matrix):
        new_matrix.append([])
        for j, y in enumerate(x):
            new_matrix[i].append(y ** 2)
    return new_matrix
