# 9-1 restaurant

class Restaurant:
    """Ultra-realistic and highly detailed restaurant simulation"""

    def __init__(self, restaurant_name, cuisine_type):
        """Init name and attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Gives a detailed four page description of the restaurant."""
        print(f"{self.restaurant_name} is a fancy restaurant that specializes in {self.cuisine_type} food.")

    def open_restaurant(self):
        """For a message to let folks know the restaurant is open"""
        print(f"{self.restaurant_name} is now open! \nPlease form orderly queues. \nFighting is not allowed. \nWait times are approximately 4 hours.")

restaurant = Restaurant('Jinju\'s', 'Korean')

print(f"The restaurant's name is {restaurant.restaurant_name}")

print(f"The restaurant serves {restaurant.cuisine_type}")

restaurant.describe_restaurant()

restaurant.open_restaurant()