#!/usr/bin/python3
"""Defines a class student"""


class Student:
    """Class student that defines a student"""

    def __init__(self, first_name, last_name, age):
        
        """Defines a student by:
            @first_name
            @last_name
            @age"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation"""
        return (self.__dict__)
