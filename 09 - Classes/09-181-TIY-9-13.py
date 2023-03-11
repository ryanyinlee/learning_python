from random import randint

class Die:
    """Simulation of a dice"""
    def __init__(self, sides):
        self.sides = 6

    def roll_die(self):
        sides_to_roll = self.sides
        result = randint(1, sides_to_roll)
        print(f"\n Your die rolled a {result}")


new_die = Die(6)
x = 10
while x > 0:
    new_die.roll_die()
    x = x - 1
