#!/usr/bin/python3
"""Defines a function that adds 2 integers"""

def add_integer(a, b=98):
    """This function adds two integers.


    Args:
        a (int or float): The first number
        b (int or flaot): The second number with default = 98.



    Returns:
        int: the sum a and b


    Raises:
        TypeError if a or b is not int or flaot
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
