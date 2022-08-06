#!/usr/bin/python3
''' base.py
'''


import json


class Base:
    ''' Base class'''
    __nb_objects = 0

    def __init__(self, id=None):
        ''' Base constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)
