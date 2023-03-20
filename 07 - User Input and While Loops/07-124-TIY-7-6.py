# 7-6 three exits

pizza = []

prompt = "Hello CONSUMER please enter the Pizzaz Pizza by Pazuzu how many toppings you desire: "
prompt += "\nNUMBER OF TOPPINGS: "

prompt1 = "Hello CONSUMER now please enter the toppings you desire: "
prompt1 += "\nAfter finishing, please type quit for a pizza summary. \nTOPPING: "

def toppingLoop():
    toppingnumber = input(prompt)
    toppingnumber = int(toppingnumber)

    toppingconfirm = input(f"You want to have {toppingnumber} toppings?\nYES/NO?:")

    if toppingconfirm == "yes" or toppingconfirm == "y":
        while toppingnumber > 0:
                
                topping = input(prompt1)

                if topping == 'quit':
                    print(f"Your pizza has the following toppings: ")
                    for topping in pizza:
                        print(f"\t{topping.title()}")
                    break
                
                else:
                    pizza.append(topping)
                    #print(pizza)
                    print(f"We have added {topping} to your pizza.\n")
                    toppingnumber = toppingnumber - 1
                    
                    if toppingnumber == 0:
                        print(f"Your pizza has the following toppings: ")
                        for topping in pizza:
                            print(f"\t{topping.title()}")
                        break
                    print(f"\nTOPPINGS LEFT {toppingnumber}")
                    
    elif toppingconfirm == "no" or toppingconfirm == "n":
        toppingLoop()
    else:
        print(f"Sorry, I don't understand.")

toppingLoop()