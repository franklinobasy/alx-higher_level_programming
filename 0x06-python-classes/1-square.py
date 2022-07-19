#!/usr/bin/python3
''' A class Square that defines a square by:
    Private instance attribute: size
    Instantiation with size (no type/value verification)
'''


class Square():
    '''class constructor'''
    def __init__(self, size):
        self.__size = size
