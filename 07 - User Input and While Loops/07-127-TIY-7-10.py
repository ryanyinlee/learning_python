#7-9 dream vacation

responses = {}

polling_active = True

while polling_active:
    name = input("What is your name?\n")
    response = input("If you could plan a dream vacation, where would you go?\n")

    responses[name] = response

    repeat = input("Would you like to let someone else take the survey?")
    if repeat == "no" or repeat == "n":
        polling_active = False
    else:
        print("I'm just gonna interpret that as a yes.")

print(f"Polling complete. Here are the results:")
for name, response in responses.items():
    print(f"{name.title()} wished to vacation in/at {response.title()}")