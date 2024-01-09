#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student class definition"""

    def __init__(self, first_name, last_name, age):
        """Initializes instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves retrieves a dictionary representation
        of a Student instance"""
        name = {}

        if attrs is None:
            return (self.__dict__)

        for key in attrs:
            """Return None if key is not found in the class else,
            a dictionary should be retrieve"""
            value = self.__dict__.get(key)
            if value is not None:
                name[key] = value

        return (name)
