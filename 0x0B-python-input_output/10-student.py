#!/usr/bin/python3
'''10-student.py
'''


class Student:
    ''' Student class '''

    def __init__(self, first_name, last_name, age):
        ''' Constructor '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' Method that returns directory description with filter '''

        if isinstance(attrs, list):
            if all(isinstance(attr, str) for attr in attrs):
                res = {}
                for i in attrs:
                    if i in self.__dict__:
                        res[i] = self.__dict__[i]
                return res
        return self.__dict__
