#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    for k, v in a_dictionary.items():
        a_dictionary[k] = 2 * v
    return a_dictionary
