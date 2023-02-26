#4-10
pizzas = ['cheese','pepperoni', 'combo', 'hawaiian', 'montenegro']
print("The First three items in the list are: ")
print(pizzas[:3])

print("The three in the middle are: ")
print(pizzas[1:4])

print("The last three items are: ")
print(pizzas[2:5])

friend_pizzas = pizzas[:]

pizzas.append("hamburger")

friend_pizzas.append("taco")

for pizza in pizzas:
    print(f"my pizza list has {pizza}")


for pizza in friend_pizzas:
    print(f"friend_pizzas list has {pizza}")