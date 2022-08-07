#!/usr/bin/python3
''' base.py
'''


from fileinput import filename
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

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string representation of list_objs to a file'''
        json_list = []

        for obj in list_objs:
            json_list.append(obj.to_dictionary())

        file_name = f"{cls.__name__}.json"
        json_string = cls.to_json_string(json_list)

        with open(file_name, "w") as file_object:
            file_object.write(json_string)
