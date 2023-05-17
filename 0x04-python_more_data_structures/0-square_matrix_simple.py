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

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(square_matrix_simple())
print(matrix)
