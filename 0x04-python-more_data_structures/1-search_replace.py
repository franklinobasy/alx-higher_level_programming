#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    if search in my_list:
        s_index = my_list.index(search)
        new_list[s_index] = replace    
    return new_list
    