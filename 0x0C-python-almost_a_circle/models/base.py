#!/usr/bin/python3
"""Defines a base class with private instance attribute"""
import json
import csv
import turtle


class Base:
    """"Base class serving as the foundation for other classes.

    Attributes:
        __nb_objects (int): Private class attribute to keep
        track of the number of objects.

    Methods:
       -__init__(self, id=None): Class constructor to initialize
        the object with an id.
       -to_json_string(list_dictionaries): Static method to return the
       JSON string representation of a list of dictionaries.
       -save_to_file(cls, list_objs): Class method to write the JSON
       string representation of list_objs to a file.
       -from_json_string(json_string): Static method to return the
       list represented by a JSON string.
       -create(cls, **dictionary): Class method to create an
       instance with attributes set using the provided dictionary.
       -update(self, *args, **kwargs): Method to update the instance
       attributes based on provided arguments.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor for Base.

        Args:
            - id (int, optional): Unique identifier for the object.
            """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method to return the JSON
        string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): List of dictionaries.

        Returns:
            str: JSON string representation of a list of dictionaries.
        """

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method to write the JSON string
        representation of list_objs to a file.

        Args:
            list_objs (list): List of instances inheriting from Base.

        Returns:
            None
        """
        if list_objs is None:
            list_objs = []
        dict_list = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dict_list)
        filename = cls.__name__ + ".json"

        with open(filename, 'w') as file:
            file.write(json_string)

    def from_json_string(json_string):
        """Static method to return the list
        represented by a JSON string.

        Args:
            json_string (str): JSON string representing
            a list of dictionaries.

        Returns:
            list: List represented by the JSON string.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Class method to create an instance with attributes
        set according to the provided dictionary.

        Args:
            **dictionary: Dictionary representing attributes for the instance.

        Returns:
            Base: Instance with attributes set according to the dictionary.
        """

        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Class method to load instances from a JSON file and return a
        list of those instances.


        Returns:
            list: List of instances loaded from the JSON file.
        """

        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                dict_list = cls.from_json_string(json_string)
                instances = [cls.create(**d) for d in dict_list]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Class method to serialize list_objs to a CSV file.

        Args:
            list_objs (list): List of instances inheriting from Base.

        Returns:
            None
        """

        if list_objs is None or len(list_objs) == 0:
            return

        filename = f"{cls.__name__}.csv"

        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([
                        obj.id,
                        obj.width,
                        obj.height,
                        obj.x,
                        obj.y
                        ])
                elif cls.__name__ == "Square":
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Class method to deserialize instances from a CSV file.

        Returns:
            list: List of instances loaded from the CSV file.
        """

        filename = f"{cls.__name__}.csv"
        instances = []

        try:
            with open(filename, mode='r') as file:
                reader = csv.reader(file)

                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(
                                id=int(row[0]),
                                width=int(row[1]),
                                height=int(row[2]),
                                x=int(row[3]),
                                y=int(row[4])
                                )
                    elif cls.__name__ == "Square":
                        obj = cls(
                                id=int(row[0]),
                                size=int(row[1]),
                                x=int(row[2]),
                                y=int(row[3])
                                )
                    else:
                        raise ValueError("Unsupported class")

                    instances.append(obj)

        except FileNotFoundError:
            pass

        return instances

    """@staticmethod
    def draw(list_rectangles, list_squares):
       Static method to open a window and draw all the Rectangles
       and Squares using Turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.

        Returns:
            None

        turtle.speed(2)

        # Drawin rectangles
        for rectangle in list_rectangles:
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)
            turtle.forward(rectangle.width)
            turtle.left(90)
            turtle.forward(rectangle.height)
            turtle.left(90)

        # Drawing Squares
        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.exitonclick()"""

    '''@staticmethod
    def draw(list_rectangles, list_squares):
        """
        Static method to open a window and draw all the
        Rectangles and Squares using Turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.

        Returns:
            None
        """
        turtle.speed(2)

        # Draw rectangles with different colors
        for i, rectangle in enumerate(list_rectangles):
            turtle.penup()
            turtle.goto(rectangle.x, rectangle.y)
            turtle.pendown()

            # Set a different color for each rectangle
            turtle.color("blue" if i % 2 == 0 else "red")
            turtle.begin_fill()

            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)

            turtle.end_fill()

        # Draw squares with different colors
        for i, square in enumerate(list_squares):
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()

            # Set a different color for each square
            turtle.color("green" if i % 2 == 0 else "purple")
            turtle.begin_fill()

            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

            turtle.end_fill()

        turtle.exitonclick()'''

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Static method to open a window and draw all the
        Rectangles and Squares using Turtle graphics.

        Args:
            list_rectangles (list): List of Rectangle instances.
            list_squares (list): List of Square instances.

        Returns:
            None
        """
        turtle.speed(2)  # Adjust the speed as needed

        # Drawing rectangles with different colors
        for i, rectangle in enumerate(list_rectangles):
            turtle.penup()
            turtle.goto(rectangle.x + i * 50, rectangle.y)
            turtle.pendown()

            # Set a different color for each rectangle
            turtle.color("blue" if i % 2 == 0 else "red")
            turtle.begin_fill()

            for _ in range(2):
                turtle.forward(rectangle.width)
                turtle.left(90)
                turtle.forward(rectangle.height)
                turtle.left(90)

            turtle.end_fill()

        # Draw squares with different colors
        for i, square in enumerate(list_squares):
            turtle.penup()
            turtle.goto(square.x + i * 50, square.y)
            turtle.pendown()

            # Set a different color for each square
            turtle.color("green" if i % 2 == 0 else "purple")
            turtle.begin_fill()

            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

            turtle.end_fill()

        turtle.exitonclick()
