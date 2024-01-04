#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """This class defines a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle(default is 0).
            height(int): The height of the rectangle(default is 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle

        Returns:
            - int: The width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle

        Args:
            - value (int): The new width value
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle.

        Returns:
            - int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            - value (int): The new height value.

        Raises:
            - TypeError: If height is not an integer.
            - ValueError: If height is less than 0.
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
