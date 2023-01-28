#!/usr/bin/python3
"""
Integers add
a and b must be integers
otherwise raise TypeError
"""
def add_integer(a, b=98):
    """
    Adds two integers
    a and b must be integers
    Raise TypeError otherwise
    Return: addition of a and b, after caster
    to integers if thery are float
    """
    if (type(a) not in [float, int]):
        raise TypeError("a must be an integer")

    if (type(b) not in [float, int]):
        raise TypeError("b must be an integer")
    return (int(a + b))
