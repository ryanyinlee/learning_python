toppings_avail = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

toppings_want = ['mushrooms', 'anchovies', 'extra cheese']

for topping in toppings_want:
    if topping in toppings_avail:
        print(f"Adding {topping}")
    else:
        print(f"Breh we ain't got no {topping}")