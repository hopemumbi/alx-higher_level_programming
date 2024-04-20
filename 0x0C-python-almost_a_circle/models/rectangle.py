#!/usr/bin/python3
""" Defines a class Rectangle """

from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes an instance of Rectangle """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        # Call the superclass's __init__ method with the id argument
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Prints out the Rectangle to stdout using `#` """
        print('\n' * self.y, end="")
        for h in range(self.height):
            print(' ' * self.x, '#' * self.width)

    def __str__(self):
        """Overides the __str__ method"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
               f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args and len(args) > 0:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for i, attr in enumerate(attributes):
                if i < len(args):
                    setattr(self, attr, args[i])

        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
