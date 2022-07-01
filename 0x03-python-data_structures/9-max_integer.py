#!/usr/bin/python3
def max_integer(my_list=[]):
    n = len(my_list)
    if n < 1:
        return None
    else:
        max = my_list[0]
        for i in range(1, n):
            if my_list[i] > max:
                max = my_list[i]

        return max
