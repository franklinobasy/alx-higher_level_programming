#!/usr/bin/python3
''' base.py
'''


import json
import turtle

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
        ''' returns the JSON string representation of list_dictionaries '''
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        ''' returns the list of the JSON string representation json_string '''
        if json_string:
            return json.loads(json_string)
        return list()

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

    @classmethod
    def create(cls, **dictionary):
        ''' returns an instance with all attributes already set '''
        obj = cls(1, 1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        ''' returns a list of instances from file'''
        try:
            with open(f"{cls.__name__}.json", 'r') as file_object:
                json_string = file_object.read()

            obj_dicts = cls.from_json_string(json_string)
            obj_list = list()

            for obj_dict in obj_dicts:
                obj_list.append(cls.create(**obj_dict))

            return obj_list

        except FileNotFoundError:
            return list()

    @classmethod
    def save_to_file_csv(cls, list_objs):
        " serializes to CSV"
        to_write = ""
        for obj in list_objs:
            obj_dict = obj.to_dictionary()
            if "size" in obj_dict.keys():
                attrs = ["id", "size", "x", "y"]
            else:
                attrs = ["id", "width", "height", "x", "y"]
            for attr in attrs:
                if attr == "y":
                    to_write += f"{obj_dict[attr]}"
                else:
                    to_write += f"{obj_dict[attr]},"
            to_write += "\n"

        file_name = f"{cls.__name__}.csv"
        with open(file_name, "w") as file_obj:
            file_obj.write(to_write)

    @classmethod
    def load_from_file_csv(cls):
        ''' deserializes from CSV'''
        try:
            with open(f"{cls.__name__}.csv", 'r') as file_object:
                csv_strings = file_object.readlines()

            if cls.__name__ == "Square":
                attrs = ["id", "size", "x", "y"]
            else:
                attrs = ["id", "width", "height", "x", "y"]

            objs_list = []
            for csv_string in csv_strings:
                values = csv_string.split(',')
                values = [int(val) for val in values]
                obj_dict = {}
                for index in range(len(values)):
                    obj_dict[attrs[index]] = values[index]

                obj = cls.create(**obj_dict)
                objs_list.append(obj)

            return objs_list

        except FileNotFoundError:
            return list()
