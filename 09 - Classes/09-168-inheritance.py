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

class ElectricCar(Car):
    """A car, but electric"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """Print a statement descrining the battery size"""
        print(f"This car has a battery size of {self.battery_size}-kWh")

    def fill_gas_tank(self):
        print(f"It ain't got no gas in it.")

car0 = Car('subaru', 'crosstrek', 2021)

tesla0 = ElectricCar('tesla', 'model x', 2019)

print(tesla0.get_descriptive_name())

tesla0.describe_battery()

tesla0.fill_gas_tank()

car0.fill_gas_tank()