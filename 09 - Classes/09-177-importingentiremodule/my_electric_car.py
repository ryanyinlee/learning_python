import car

my_car = car.Car('Subaru', 'Crosstrek', 2021)

my_electric_car = car.ElectricCar('Rivian', 'Chonk', 2025)

print(my_car.get_descriptive_name())

print(my_electric_car.get_descriptive_name())