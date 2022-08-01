#!/usr/bin/python3
"""2-is_same_class.py
"""


def is_same_class(obj, a_class):
    """ Compare is obj is exactly an instance of a_class """
    return type(obj) == a_class
