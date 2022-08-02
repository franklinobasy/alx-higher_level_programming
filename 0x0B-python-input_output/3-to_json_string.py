#!/usr/bin/python3
'''5-to_json_string.py
'''

import json


def to_json_string(my_obj):
    ''' returns the JSON representation of an object '''

    return json.dump(my_obj)
