prompt = "\nEnter some text and I'll parrot it to you."

prompt += "\nEnter 'quit' to leave the program."

prompt += "\nPARROT: "

message = ""

while message != 'quit':
    message = input(prompt)
    
    if message !="quit":
        print(message)