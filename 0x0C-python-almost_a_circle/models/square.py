#!/usr/bin/python3
'''square.py
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Sqaure class'''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Square constructor '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
