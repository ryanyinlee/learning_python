def make_pizza(size, *toppings):
    """Print a list of requested toppings"""
    print(f"\nMaking a {size}\" pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")


make_pizza(14, 'pepo')

make_pizza(10, 'mushrooms', 'green peppers', 'extra extra ches')