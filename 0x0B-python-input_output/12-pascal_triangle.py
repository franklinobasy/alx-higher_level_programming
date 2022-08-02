#!/usr/bin/python3
'''12-pascal_triangle.py
'''


def pascal_triangle(n):
    '''
    returns a list of lists of integers representing
    the Pascal’s triangle of n
    '''

    triangle = [[1], [1, 1]]
    if n <= 0:
        return []

    if n == 1:
        return [[1]]

    for term in range(3, n + 1):
        temp = []
        last_term = triangle[-1]
        for i in range(len(last_term)- 1):
            sum_ = last_term[i] + last_term[i + 1]
            temp.append(sum_)
        temp.insert(0, 1)
        temp.append(1)
        triangle.append(temp)
    return triangle
