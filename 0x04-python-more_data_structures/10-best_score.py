#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_v = max(list(a_dictionary.values()))
    for k, v in a_dictionary.items():
        if v == max_v:
            return k
    return None
