#!/usr/bin/python3
'''square.py
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Sqaure class'''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Square constructor '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' size getter'''
        return self.width

    @size.setter
    def size(self, value):
        ''' size setter'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"


    def update(self, *args, **kwargs):
        if args:
            attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if attr[i] == 'size':
                    setattr(self, "width", args[i])
                    setattr(self, "height", args[i])
                else:
                    setattr(self, attr[i], args[i])
        else:
            for k, v in kwargs.items():
                if k == "size":
                    setattr(self, "width", v)
                    setattr(self, "height", v)
                else:
                    if hasattr(self, k):
                        setattr(self, k, v)
