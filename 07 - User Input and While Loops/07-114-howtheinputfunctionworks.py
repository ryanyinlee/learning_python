message = input("Tell me something, and I will repeat it\n")

print(f"You wanted me to say {message.upper()}")

reply = input(f"Since you had me say {message}, why not repeat what you said?\n")

if reply.lower() == message.lower():
    print(f"You did it!")
else:
    print(f"Failure.")