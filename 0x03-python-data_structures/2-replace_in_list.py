#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    n = len(my_list)
    if idx < 0 or idx >= n:
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
