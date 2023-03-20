#5-8 hello admin

usernames = ['admin', 'adam', 'steven', 'eliza', 'melissa']

for user in usernames:
    if user == 'admin':
        print(f"Hello ADMIN, what up.")
    else:
        print(f"Hello there {user.title()}")


