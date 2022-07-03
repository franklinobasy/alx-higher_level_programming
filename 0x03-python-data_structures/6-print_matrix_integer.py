#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        print()
    else:
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if col == len(matrix[row]) - 1:
                    end = "\n"
                else:
                    end = " "
                print("{:d}".format(matrix[row][col]), end=end)
