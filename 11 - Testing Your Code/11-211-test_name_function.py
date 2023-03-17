import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests name_function.py"""

    def test_first_last_name(self):
        """Basic name test."""
        formatted_name = get_formatted_name('Jim', 'Bob')
        self.assertEqual(formatted_name, 'Jim Bob')

    def test_first_last_middle_name(self):
        """Test full names with middle name"""
        formatted_name = get_formatted_name('Dirk', 'Gently', 'Smith')
        self.assertEqual(formatted_name, 'Dirk Smith Gently')

if __name__ == '__main__':
    unittest.main()

