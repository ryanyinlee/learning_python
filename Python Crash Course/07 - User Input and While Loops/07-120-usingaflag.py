prompt = "\nEnter some text and I'll parrot it to you."

prompt += "\nEnter 'quit' to leave the program."

prompt += "\nPARROT: "

active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)