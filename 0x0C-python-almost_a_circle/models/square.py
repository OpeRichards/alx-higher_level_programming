#!/usr/bin/python3
"""This defines a class ``Square``."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """This class ``Square`` inherits from class ``Rectangle``."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new instance of the class ``Square``.
        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square.
                            Defaults to 0.
            y (int, optional): The y-coordinate of the square.
                            Defaults to 0.
            id (int, optional): A specific id to assign to the instance.
                                Inherited from the ``Rectangle`` class.
    """
        self.size = size
        super().__init__(size, size, x, y, id)
        self.x = x
        self.y = y

    @property
    def size(self):
        """Getter for the size of the square."""
        return self.__width

    @size.setter
    def size(self, value):
        """Sets the size value."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """Returns the string representation of square instance."""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))

    def update(self, *args, **kwargs):
        """This method assigns variable attributes.
        Args:
            *args: Variable number of arguments consisting any of \
                (id, width, height, x and y)
            **kwargs: Variable number of key/value pairs.
        Returns:
            The return statement is handled by __str__ method
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Method to return the dictionary representation of a Square.
        Args:
            id, width, height, x, y
        Returns:
            the dictionary representation of a Square.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}