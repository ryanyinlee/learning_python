import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Makes sure the city country function works properly"""

    def test_city_country(self):
        """Simple test of a city and country"""
        formatted_city = city_country("Reykjavik", "Iceland")
        self.assertEqual(formatted_city, "Reykjavik, Iceland")

    def test_city_country_population(self):
        """Test a city, country AND population."""
        formatted_city = city_country('Reykjavik', 'Iceland', 122000)
        self.assertEqual(formatted_city, 'Reykjavik, Iceland Population: 122000')


if __name__ == '__main__':
    unittest.main()