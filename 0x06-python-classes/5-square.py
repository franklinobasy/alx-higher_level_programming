#!/usr/bin/python3
""" Class Square that defines a square by
    Private instance attribute: size
    Public instance method: def my_print(self):
        that prints in stdout the square with the character #:
        - if size is equal to 0, print an empty line
"""


class Square():
    """Class constructor"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """size getter"""
    @property
    def size(self):
        return self.__size

    """size setter"""
    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    """returns the current area of square"""
    def area(self):
        return self.__size ** 2

    """prints in stdout the square with the character #"""
    def my_print(self):
        if self.__size:
            for _ in range(self.__size):
                print("#" * self.__size)
        else:
            print()
