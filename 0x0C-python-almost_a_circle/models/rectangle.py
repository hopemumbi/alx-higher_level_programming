#!/usr/bin/python3
""" Defines a Rectangle class. """
from models.base import Base


class Rectangle(Base):
    """Represents a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes an instance of Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x coordinate of the rectangle.
            y (int): The y coordinate of the rectangle.
            id (int): The identity of an instance of Rectangle.

        Raises:
            TypeError: If width/height/x/y are not int`s.
            ValueError: : If either height or width are <= 0.
            ValueError: If x or y are < 0.

        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set/get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Set/get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of a rectangle"""
        return self.width * self.height

    def display(self):
        """Print out the Rectangle to stdout using `#` """
        print('\n' * self.y, end="")
        for h in range(self.height):
            print(' ' * self.x, '#' * self.width)

    def __str__(self):
        """Print a dictionary representation of a Rectangle
        Overides the __str__ method
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
               f"{self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Update attributes
        Args:
            *args (ints): New attribute values.
                - 1st argument should be the id attribute
                - 2nd argument should be the width attribute
                - 3rd argument should be the height attribute
                - 4th argument should be the x attribute
                - 5th argument should be the y attribute
            **kwargs (dict): key/value pairs
        """
        # If *args is provided and contains values
        if args and len(args) > 0:
            # Define the order of attributes to be updated
            attributes = ['id', 'width', 'height', 'x', 'y']
            # Iterate over the provided arguments and set attributes
            for i, attr in enumerate(attributes):
                if i < len(args):
                    setattr(self, attr, args[i])

        # If **kwargs is provided and contains key-value pairs
        elif kwargs and len(kwargs) > 0:
            # Iterate over the key-value pairs and set attributes
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.width,
                "height": self.height, "x": self.x, "y": self.y}
