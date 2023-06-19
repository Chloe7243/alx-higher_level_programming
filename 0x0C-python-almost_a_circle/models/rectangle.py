#!/usr/bin/python3
""" A class called Rectangle """
from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""

    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("width must be > 0")
        if value is not int or value is not float:
            raise TypeError("width must be an integer")
        self.__width = int(value) if value is float else value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("height must be > 0")
        if value is not int or value is not float:
            raise TypeError("height must be an integer")
        self.__height = int(value) if value is float else value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        if value is not int or value is not float:
            raise TypeError("x must be an integer")
        self.__x = int(value) if value is float else value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        if value is not int or value is not float:
            raise TypeError("y must be an integer")
        self.__y = int(value) if value is float else value


if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
