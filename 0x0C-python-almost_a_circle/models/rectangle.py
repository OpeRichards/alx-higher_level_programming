#!/usr/bin/python3
"""This defines a class ``Rectangle``."""


from models.base import Base


class Rectangle(Base):
    """class Rectangle inherits from Base."""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  # Call the Base class constructor with id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance.
        Args:
            self.__width: Width of rectangle.
            self.__height: Height of rectangle.
        Returns:
            area (int): Result of product of width and height.
        """
        return self.__width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """Create a string method."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute at instantiation.
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
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Method to return the dictionary representation of a Rectangle.
        Args:
            id, width, height, x, y
        Returns:
            the dictionary representation of a Rectangle.
        """
        return {'id': self.id, 'width': self.width, 'height': self.height,
                'x': self.x, 'y': self.y}
