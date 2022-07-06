#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    items = list(a_dictionary.items()).copy()
    for k, v in items:
        if v == value:
            del a_dictionary[k]

    return a_dictionary
