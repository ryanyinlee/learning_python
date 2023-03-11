from car import Car as C
from electric_car import ElectricCar as EC

my_car = C('Subaru', 'Crosstrek', 2021)

my_electric = EC('Rivian', 'Hog', 2024)

print(my_car.get_descriptive_name())

print(my_electric.get_descriptive_name())