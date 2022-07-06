#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    n = len(my_list)
    for s_index in range(n):
        if my_list[s_index] == search:
            new_list[s_index] = replace
    return new_list
