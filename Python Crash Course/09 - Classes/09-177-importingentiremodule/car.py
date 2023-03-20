"""A class that can be used to represent gas cars, electric cars, and their batteries"""

class Car:
    """A 100%, down to the last bolt, accurate representation of a car."""

    def __init__(self, make, model, year):
        """Init the car attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Displays car's mileage"""
        print(f"The {self.get_descriptive_name()} has {self.odometer} miles on it.")    
    
    def update_odometer(self, mileage):
        """Updates the odometer"""
        if mileage >= self.odometer:
            self.odometer = mileage
        else: 
            print("Odometer can't be given lower value.")
    
    def increment_odometer(self, miles):
        """Add a the inputted amount to the odometer."""
        self.odometer += miles

    def fill_gas_tank(self):
        print(f"Tank filled.")

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