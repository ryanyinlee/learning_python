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
    

newcar0 = Car('Subaru', 'Crosstrek', 2021)

print(newcar0.get_descriptive_name())

newcar0.update_odometer(4401)

newcar0.read_odometer()

newcar0.update_odometer(4000)
