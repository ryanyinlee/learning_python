responses = {}

polling_active = True

while polling_active:
    name = input("\nWhat ur name?")
    response = input("\nWhich mountain would you like to climb?")


    responses[name] = response

    repeat = input("Would you like to let another person respond? Y/N)")

    if repeat == "no":
        polling_active = False
    

for name, response in responses.items():
    print(f"\n{name} wants to climb {response}")