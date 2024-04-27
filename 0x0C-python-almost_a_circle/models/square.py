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
        self.__width = value
        self.__height = value

    def __str__(self):
        """Returns the string representation of square instance."""
        return ("[Square] ({}) {}/{} - {}".format
                (self.id, self.x, self.y, self.size))
