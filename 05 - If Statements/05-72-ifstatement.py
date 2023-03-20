cars = ["audi","bmw","subaru","toyota"]

for car in cars:
    if car == 'subaru':
        print(f"Oh haha dank, I drive a {car.title()}")
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
    

car = 'audi'
if car == 'bmw':
    print("This was true.")
else:
    print("This was false.")


car = 'audi'
if car == 'audi':
    print("This was true.")
else:
    print("This was false.")

car = 'audi'
if car == 'Audi':
    print("This was true.")
else:
    print("This was false.")


car = 'Audi'
if car.lower() == 'audi':
    print("This was true.")
else:
    print("This was false.")

