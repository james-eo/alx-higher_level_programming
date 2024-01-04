#!/usr/bin/python3

class Rectangle:
    """
    This class defines a rectangle.

    Attributes:
    - _width (int): The width of the rectangle (default is 0).
        - _height (int): The height of the rectangle (default is 0).

    Methods:
        - __init__(self, width=0, height=0): Initializes a
         new Rectangle instance.
        - width (property): Retrieves the width of the rectangle.
        - width (setter): Sets the width of the rectangle.
        - height (property): Retrieves the height of the rectangle.
        - height (setter): Sets the height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Args:
            - width (int): The width of the rectangle
            must be an integer(default is 0).
            - height(int): The height of the rectangle
            must be an integer(default is 0)

        """
        self.__height = 0
        self.__width = 0
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Retrieves the width of the rectangle

        Returns:
            - int: The width of the rectangle
        """

        return self.width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

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
        """
        Retrieves the height of the rectangle.

        Returns:
            - int: The height of the rectangle

        """
        return self.height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

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
