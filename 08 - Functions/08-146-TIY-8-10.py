#8-10 sending messages

messages = ['ay wassup', 'how u doin bby', 'where u at bru', 'you okay man?', 'have you seen my dog?']

def show_messages(messages):
    """Prints text messages inputted."""
    for message in messages:
        print(message)

show_messages(messages)

def send_messages(messages, sent_messages):
    """Receives text messages and moves them to a new list"""
    while messages:
        message = messages.pop()
        print(message)
        sent_messages.append(message)
    
    print(messages)
    print(sent_messages)

sent = []

send_messages(messages, sent)