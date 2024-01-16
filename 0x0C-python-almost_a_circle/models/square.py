#!/use/bin/python3

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square inherits from Rectangle class

    Attribute:
        id (int): Identifier for the square.
        __size (int): Size of the square.
        __x (int): X-coordinate of the square.
        __y (int): Y-coordinate of the square.


    Methods:
        Methods:
        __init__(self, size, x=0, y=0, id=None): Class constructor
        to initialize square attributes.
        __str__(self): Overridden method to return a
        string representation of the Square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialisses a Square object with the given size
        and coordinates


        Args:
            size (int): Size of the square.
            x (int, optional): X-coordinate of the square(Default is 0)
            y (int, optional): Y-coordinate of the square(Default is 0)
            id (int, optional): Identifier for the square.
            If not provided, it is assigned by the Base class.
        """

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for the size attribute."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for the size attribute."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Public method to assign arguments and
        key-worded arguments to attributes.
        """

        """if args:
            # self.id,self.size, self.x, self.y = args
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.size = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def __str__(self):
        """Overridden method to return a string
        representation of the Square.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def to_dictionary(self):
        """Returns the dictionary representation of
        the Square class
        """

        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
