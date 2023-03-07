def make_pizzaX(*toppings):
    """Print a list of requested toppings"""
    print(toppings)



def make_pizza(*toppings):
    """Print a list of requested toppings"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")


make_pizza('pepo')

make_pizza('mushrooms', 'green peppers', 'extra extra ches')