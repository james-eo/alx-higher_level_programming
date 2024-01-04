#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """This class defines a rectangle.

    Attributes:
    - __width (int): The width of the rectangle (default is 0).
    - __height (int): The height of the rectangle (default is 0).
    - number_of_instances (class attribute): Tracks the
    number of instances of Rectangle.

    Methods:
    - __init__(self, width=0, height=0): Initializes a new Rectangle instance.
    - width (property): Retrieves the width of the rectangle.
    - width (setter): Sets the width of the rectangle.
    - height (property): Retrieves the height of the rectangle.
    - height (setter): Sets the height of the rectangle.
    - area(self): Calculates and returns the area of the rectangle.
    - perimeter(self): Calculates and returns the perimeter of the rectangle.
    - __str__(self): Returns a string representation of the rectangle.
    - __repr__(self): Returns a string representation
    of the rectangle for recreation.
    - __del__(self): Prints a farewell message when rectangle is deleted.
    """

    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle(default is 0).
            height(int): The height of the rectangle(default is 0)
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Sets and Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets/Sets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defines the area of a Reectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Defines the perimeter of Rectangle"""
        if (self.__width == 0) or (self.__height == 0):
            return 0
        else:
            return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        """Returns a string representation('#') of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_lines = []

        for _ in range(self.__height):
            rectangle_lines.append('#' * self.__width)
        return "\n".join(rectangle_lines)

    def __repr__(self):
        """Returns a string representation of the rectangle for recreation.

        Returns:
            - str: A string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(sefl):
        """Prints farewell message when rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
