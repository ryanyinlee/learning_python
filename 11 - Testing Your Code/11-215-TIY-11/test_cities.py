import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Makes sure the city country function works properly"""

    def test_city_country(self):
        """Simple test of a city and country"""
        formatted_city = city_country("Reykjavik", "Iceland")
        self.assertEqual(formatted_city, "Reykjavik, Iceland")

if __name__ == '__main__':
    unittest.main()