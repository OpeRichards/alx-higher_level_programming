#!/usr/bin/python3
"""Unittest for ``rectangle`` module."""


import unittest
import inspect
import os
import pycodestyle

from models.base import Base
from models.rectangle import Rectangle

class TestMaxInteger(unittest.TestCase):
    """Test cases for the Rectangle class."""
    
    def test_shebang_present_first_line(self):
        """Test if the first line contains #!/usr/bin/python3."""
        with open('models/rectangle.py', 'r') as f:
            first_line = f.readline().strip()
        self.assertEqual(first_line, '#!/usr/bin/python3')

    def test_documentation(self):
        """Test if everything is documented in models/rectangle.py."""
        path = 'models/rectangle.py'
        self.assertTrue(os.path.exists(path), 'File not found')
        with open(path, 'r') as file:
            content = file.read()

    def test_create_instance(self):
        """Test if an instance of Rectangle can be created."""
        r = Rectangle(5, 10)
        self.assertIsInstance(r, Rectangle)
    
    def test_create_instance_with_x(self):
        """Test if an instance of Rectangle can be created with x."""
        r = Rectangle(5, 10, 2)
        self.assertIsInstance(r, Rectangle)

    def test_create_instance_with_y(self):
        """Test if an instance of Rectangle can be created with y."""
        r = Rectangle(5, 10, 2, 4)
        self.assertIsInstance(r, Rectangle)
    
    def test_create_instance_with_id(self):
        """Test if an instance of Rectangle can be created with id."""
        r = Rectangle(5, 10, 2, 4, 1)
    #    self.RectangleIsInstance(r, Rectangle)
        self.assertEqual(r.id, 1)

    def test_width_getter_setter(self):
        """Test if Rectangle has getter and setter for width."""
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        r.width = 7
        self.assertEqual(r.width, 7)

    def test_width_private_instance(self):
        """Check if width is a private instance attribute."""
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "_Rectangle__width"))

    def test_height_getter_setter(self):
        """Test if Rectangle has getter and setter for height."""
        r = Rectangle(5, 10)
        self.assertEqual(r.height, 10)
        r.height = 15
        self.assertEqual(r.height, 15)

    def test_height_private_instance(self):
        """Check if height is a private instance attribute."""
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "_Rectangle__height"))

    def test_x_getter_setter(self):
        """Test if Rectangle has getter and setter for x."""
        r = Rectangle(5, 10, 2)
        self.assertEqual(r.x, 2)
        r.x = 7
        self.assertEqual(r.x, 7)

    def test_private_x(self):
        """Check if x is a private instance attribute."""
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "_Rectangle__x"))

    def test_y_getter_setter(self):
        """Test if Rectangle has getter and setter for y."""
        r = Rectangle(5, 10, 2, 4)
        self.assertEqual(r.y, 4)
        r.y = 7
        self.assertEqual(r.y, 7)

    def test_private_y(self):
        """Check if y is a private instance attribute."""
        r = Rectangle(1, 2)
        self.assertTrue(hasattr(r, "_Rectangle__y"))

    def test_width_type_error_on_instantiation(self):
        """Check if TypeError is raised for width during instantiation."""
        with self.assertRaises(TypeError):
            r = Rectangle("invalid", 2)

    def test_height_type_error_on_instantiation(self):
        """Check if TypeError is raised for height during instantiation."""
        with self.assertRaises(TypeError):
            r = Rectangle(1, "invalid")

    def test_x_type_error_on_instantiation(self):
        """Check if TypeError is raised for x during instantiation."""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "invalid")

    def test_y_type_error_on_instantiation(self):
        """Check if TypeError is raised for y during instantiation."""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 4, "invalid")

    def test_width_type_error_on_setter(self):
        """Check if TypeError is raised for width during setter method."""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.width = "invalid"

    def test_height_type_error_on_setter(self):
        """Check if TypeError is raised for height during setter method."""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.height = "invalid"

    def test_x_type_error_on_setter(self):
        """Check if TypeError is raised for x during setter method."""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.x = "invalid"

    def test_y_type_error_on_setter(self):
        """Check if TypeError is raised for y during setter method."""
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.y = "invalid"

    def test_width_value_error_instantiation(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_height_value_error_instantiation(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

    def test_x_value_error_instantiation(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1)

    def test_y_value_error_instantiation(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -2)

    def test_width_value_error_setter(self):
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.width = 0

    def test_height_value_error_setter(self):
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.height = 0

    def test_x_value_error_setter(self):
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.x = -1

    def test_y_value_error_setter(self):
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.y = -1

    def test_pycodestyle(self):
       """Test if models/rectangle.py follows Pycodestyle."""
       pycodestyle_errors = os.system('pycodestyle models/rectangle.py')
       self.assertEqual(pycodestyle_errors, 0) 
    

if __name__ == '__main__':
    unittest.main()
