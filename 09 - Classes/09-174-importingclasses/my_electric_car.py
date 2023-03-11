from car import ElectricCar, Car

my_electric_car = ElectricCar('Rivian', 'Heftyboi', 2026)

print(my_electric_car.get_descriptive_name())

my_electric_car.battery.describe_battery()

my_electric_car.battery.get_range()

regular_car = Car('Subaru', 'Crosstrek', 2021)

print(regular_car.get_descriptive_name())