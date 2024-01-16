#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """Rectangle class representing a rectangle shape.


    Inherits from Base.


    Attributes:
        id (int): Identifier for the rectangle.
        __width (int): Width of the rectangle.
        __height (int): Height of the rectangle.
        __x (int): X-coordinate of the rectangle.
        __y (int): Y-coordinate of the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None): Class
        constructor to initialize rectangle attributes.
        width(self): Getter method for the width attribute.
        height(self): Getter method for the height attribute.
        x(self): Getter method for the x attribute.
        y(self): Getter method for the y attribute.
        width(self, value): Setter method for the width attribute.
        height(self, value): Setter method for the height attribute.
        x(self, value): Setter method for the x attribute.
        y(self, value): Setter method for the y attribute.
        area(self): Public method to calculate
        and return the area value of the rectangle.
        display(self): Public method to print the Rectangle
        instance with the character #, considering x and y.
        __str__(self): Overridden method to return a string
        representation of the Rectangle.
        """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class constructor to initialize rectangle attributes.

        Args:
            width (int): Width of the rectangle.
            height (int): Height of the rectangle.
            x (int, optional): X-coordinate of the rectangle.
            y (int, optional): Y-coordinate of the rectangle.
            id (int, optional): Identifier for the rectangle.
            If not provided, it is assigned by the Base class.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter method for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for the width attribute."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for the height attribute."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter method for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for the x attribute."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter method for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for the y attribute."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Public method that returnd the
        area value of the Rectagle instance
        """
        return self.__width * self.__height

    def display(self):
        """Public method to print the Rectangle instance
        with the character #, considering x and y.
        """

        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Overridden method to return a string
        representation of the Rectangle.
        """

        return (
                f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}"
                )

    def update(self, *args, **kwargs):
        """Public method to assign arguments to each attribute."""

        if args:
            self.id, self.width, self.height, self.x, self.y = args
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representaion of
        the Rectangle class
        """

        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
