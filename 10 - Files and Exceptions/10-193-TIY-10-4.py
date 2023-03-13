#10-4 guestbook

filepath = '/Users/ryanlee/projects/python/10 - Files and Exceptions/text/guestbook.txt'

guestbook = True

while guestbook:
    guestname = input('Hello guest, please enter your first name.')
    print(f"Please type quit to leave.")
    
    if guestname.lower() == 'quit':
        break
    else:
        with open(filepath, 'a') as text_to_write:
            text_to_write.write(f"\n{guestname}")

        with open(filepath) as text_to_write:
            for line in text_to_write:
                print(line)