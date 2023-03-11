from car import Car

my_car = Car('Subaru', 'Crosstrek', 2021)

print(my_car.get_descriptive_name())

my_car.odometer = 4600
my_car.read_odometer()