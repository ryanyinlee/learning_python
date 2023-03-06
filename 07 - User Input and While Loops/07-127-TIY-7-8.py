#7-8 deli

sandwich_orders = ['ham', 'turkey', 'tuna', 'salami','roast beef', 'pastrammi', 'cheese' ]

finished_sandwiches = []

"""while len(sandwich_orders) > 0:
    for sandwich in sandwich_orders:
        print(f"I made your {sandwich} sando bruh")
        finished_sandwiches.append(sandwich)
        sandwich_orders.remove(sandwich)"""

while sandwich_orders:
    sandwich = sandwich_orders.pop()

    print(f"I made your {sandwich} sando bruh")
    finished_sandwiches.append(sandwich)