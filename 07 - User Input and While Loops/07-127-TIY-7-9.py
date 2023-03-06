#7-9 no pastrami

sandwich_orders = ['ham', 'turkey', 'tuna', 'pastrami', 'salami', 'roast beef', 'pastrami', 'cheese', 'pastrami' ]

finished_sandwiches = []

missing_ingredient = 'pastrami'

print(f"\nAy, we out of {missing_ingredient}\n")

while missing_ingredient in sandwich_orders:
    sandwich_orders.remove(missing_ingredient)

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your {sandwich} sando bruh\n")
    finished_sandwiches.append(sandwich)