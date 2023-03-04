users = {
    'aenstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
        'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'sorbonne',
    }
}

for username, userinfo in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{userinfo['first']} {userinfo['last']}"
    location = userinfo['location']
    print(f"\tFull Name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")