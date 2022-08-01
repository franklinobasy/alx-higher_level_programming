#!/usr/bin/python3
"""100-my_int.py
"""


class MyInt(int):
    """ __eq__ and __ne__ inverted """

    def __eq__(self, other):
        """ Inverted to not equal """
        return super().__ne__(other)

    def __ne__(self, other):
        """ Inverted to equal """
        return super().__eq__(other)
