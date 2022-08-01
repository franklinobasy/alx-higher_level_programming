#!/usr/bin/python3
"""10-square.py
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ inherits from Rectangle class """

    def __init__(self, size):
        """ Constructor """
        if self.integer_validator('size', size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Returns area of Square object"""
        return super().area()
