#!/usr/bin/python3
'''rectangle.py
'''

from models.base import Base


class Rectangle(Base):
    '''Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Rectangle constructor '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        ''' width getter'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        ''' height getter'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height setter'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        ''' x getter'''
        return self.__x

    @x.setter
    def x(self, value):
        ''' x setter'''
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        ''' y getter'''
        return self.__y

    @y.setter
    def y(self, value):
        ''' y setter'''
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def __str__(self) -> str:
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def area(self):
        ''' Returns area of Rectangle object'''
        return self.width * self.height

    def display(self):
        ''' prints in stdout the Rectangle instance with the character # '''
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * (self.x), "#" * (self.width))

    def update(self, *args):
        n = len(args)
        if n == 1:
            self.id = args[0]
        elif n == 2:
            self.id, self.width = args
        elif n == 3:
            self.id, self.width, self.height = args
        elif n == 4:
            self.id, self.width, self.height, self.x = args
        elif n == 5:
            self.id, self.width, self.height, self.x, self.y = args
        