"""A class that can be used to represent electric cars, and their batteries"""

from car import Car

class Battery:
    """A model of a battery for an electric car. 100% scientifically and philosophically accurate"""
    def __init__(self, battery_size=75):
        """Init battery attributes"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement descrining the battery size"""
        print(f"This car has a battery size of {self.battery_size}-kWh")

    def get_range(self):
        """Print a statement about battery range"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go {range} miles on a full charge.")
    
    def upgrade_battery(self):
        if self.battery_size <= 100:
            self.battery_size = 100


class ElectricCar(Car):
    """A car, but electric"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print(f"It ain't got no gas in it.")