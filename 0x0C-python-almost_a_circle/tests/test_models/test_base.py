#!/usr/bin/python3
"""Unittest for ``Base`` module."""


import unittest
import inspect
import pycodestyle

from models.base import Base

class TestBase(unittest.TestCase):
    """Define test cases for the ``Base`` function."""
    
    def test_shebang_present_in_first_line(self):
        with open('models/base.py', 'r') as f:
            first_line = f.readline().strip()
        self.assertEqual(first_line, '#!/usr/bin/python3')

    def test_no_import_statements(self):
        with open('models/base.py', 'r') as f:
            lines = f.readlines()
        import_statements = [line for line in lines if line.startswith('import') or line.startswith('from')]
        self.assertEqual(len(import_statements), 0)

    def test_class_base_exists(self):
        self.assertTrue(hasattr(Base, '__init__'))
        
    def test_module_documented(self):
        self.assertTrue('base'.__doc__)

    def test_function_documented(self):
        self.assertTrue(inspect.getdoc(Base))

    def test_create_instance_without_id(self):
        b1 = Base()
        self.assertIsInstance(b1, Base)

    def test_create_instance_with_id(self):
        b2 = Base(5)
        self.assertEqual(b2.id, 5)

    def test_assign_id_incrementally(self):
        b3 = Base()
        b4 = Base()
        self.assertEqual(b3.id, b4.id -1)
        
    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide()        
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)

 
if __name__ == '__main__':
    unittest.main()