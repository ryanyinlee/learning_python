import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Checks to make sure Employee class functions properly"""

    def setUp(self):
        """Creates a sample employee to test the Class"""
        self.test_employee0 = Employee('Jim', 'Bobly', 50_000)

    def test_employeeExist(self):
        """Make sure the employee exists and has a salary"""
        self.assertEqual(self.test_employee0.first, 'Jim')
        self.assertEqual(self.test_employee0.last, 'Bobly')
        self.assertEqual(self.test_employee0.salary, 50_000)

    def test_giveDefaultRaise(self):
        """Makes sure that giving the employee a standard raise is successful"""
        self.test_employee0.give_raise()
        self.assertEqual(self.test_employee0.salary, 55_000)

    def test_giveCustomRaise(self):
        """Makes sure that giving the employee a custom raise is successful"""
        self.test_employee0.give_custom_raise(12_000)
        self.assertEqual(self.test_employee0.salary, 62_000)

if __name__ == '__main__':
    unittest.main()