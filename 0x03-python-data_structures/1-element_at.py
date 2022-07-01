#!/usr/bin/python3
def element_at(my_list, idx):
    n = len(my_list)
    return None if (idx < 0 or idx >= n) else my_list[idx]
