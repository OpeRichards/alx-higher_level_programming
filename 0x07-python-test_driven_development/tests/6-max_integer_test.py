#!/usr/bin/python3
"""Unittest for ``mox_integer`` module."""


import unittest
import inspect
import pycodestyle

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define test cases for the ``max_integer`` function."""
    
    def test_shebang_present(self):
        with open('6-max_integer.py', 'r') as f:
            first_line = f.readline().strip()
        self.assertEqual(first_line, '#!/usr/bin/python3')

    def test_no_import_statements(self):
        with open('6-max_integer.py', 'r') as f:
            lines = f.readlines()
        import_statements = [line for line in lines if line.startswith('import') or line.startswith('from')]
        self.assertEqual(len(import_statements), 0)

    def test_module_documented(self):
        self.assertTrue(max_integer.__doc__)

    def test_function_documented(self):
        self.assertTrue(inspect.getdoc(max_integer))

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([3, 2, 1]), 3)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([2, 3, 1]), 3)

    def test_one_negative_number(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_only_negative_numbers(self):
        self.assertEqual(max_integer([-3, -2, -1]), -1)

    def test_list_of_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_pycodestyle(self):
        style = pycodestyle.StyleGuide()
        result = style.check_files(['6-max_integer.py'])
        self.assertEqual(result.total_errors, 0)
        
if __name__ == '__main__':
    unittest.main()