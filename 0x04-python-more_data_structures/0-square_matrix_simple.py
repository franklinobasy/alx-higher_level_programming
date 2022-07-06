#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_list = lambda x: [i**2 for i in x]
    new_list = []
    for row in matrix:
        new_row = sq_list(row)
        new_list.append(new_row)
    return new_list
