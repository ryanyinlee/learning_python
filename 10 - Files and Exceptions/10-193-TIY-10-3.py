#10-3 guest

filepath = '/Users/ryanlee/projects/python/10 - Files and Exceptions/text/guest.xt'

guestname = input('Hello guest, please enter your first name.')

with open(filepath, 'w') as text_to_write:
    text_to_write.write(guestname)

with open(filepath) as text_to_write:
    for line in text_to_write:
        print(line)