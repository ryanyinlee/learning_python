prompt = "\nPlease enter a city you have visited:"
prompt += "\n(Type Quit when done)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"Wow, {city.title()} seems like a dump.")