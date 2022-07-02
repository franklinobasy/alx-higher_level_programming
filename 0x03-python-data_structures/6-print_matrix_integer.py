#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n_row = len(matrix)
    n_col = len(matrix[0])
    if n_row <= 1 or n_col <= 1:
        print()
    else:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if col == 2:
                    end = "\n"
                else:
                    end = " "
                print("{:d}".format(matrix[row][col]), end=end)
