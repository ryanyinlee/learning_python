# 7-4 pizza toppings

prompt = "Hello CONSUMER please enter the Pizzaz Pizza by Aziz toppings you desire: "
prompt += "\nAfter finishing, please type quit for a pizza summary. \nTOPPING: "

pizza = []

active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        print(f"Your pizza has the following toppings: ")
        for topping in pizza:
            print(f"\t{topping.title()}")
        active = False
    else:
        pizza.append(topping)
        #print(pizza)
        print(f"We have added {topping} to your pizza.\n")