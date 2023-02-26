current_users = ['admin', 'adam', 'steven', 'eliza', 'melissa']

new_users =  ['admin2', 'adam', 'notsteven', 'eliza', 'not_melissa', 'Adam', 'ADAM']

for user in new_users:
    if user.lower() in current_users:
        print(f"Dear {user.title()}, you must change your username!")
    else:
        print(f"Username {user.title()} is available.")