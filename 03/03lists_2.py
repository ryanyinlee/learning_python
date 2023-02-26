motorcycles = ['honda', 'yamaha', 'suzooki']

print(motorcycles)

motorcycles[0] = 'poocati'

print(motorcycles)

motorcycles.append('poocati2 the poocating')

print(motorcycles)

cars = []

cars.append('toyota')
cars.append('honda')
cars.append('hyundai')
cars.append('acura')

print(cars)

cars.insert(1, 'fjord')

print(cars)

del cars[0]

print(cars)

popped_car = cars.pop()

print(cars)

print(popped_car)

front_car = cars.pop(0)

print(front_car)

cars.remove('honda')

print(cars)