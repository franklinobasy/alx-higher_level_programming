#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(sq_list, matrix))

def sq_list(x):
    return [i**2 for i in x]