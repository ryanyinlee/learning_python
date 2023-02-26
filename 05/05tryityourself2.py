#5-8 hello admin

usernames = ['admin', 'adam', 'steven', 'eliza', 'melissa']

for user in usernames:
    if user == 'admin':
        print(f"Hello ADMIN, what up.")
    else:
        print(f"Hello there {user.title()}")

#5-9 No Users

usernames = []

if usernames:
    for user in usernames:
        if user == 'admin':
            print(f"Hello ADMIN, what up.")
        else:
            print(f"Hello there {user.title()}")
else:
    print("No one is logged on.")

#5-10 Checking UserNames

