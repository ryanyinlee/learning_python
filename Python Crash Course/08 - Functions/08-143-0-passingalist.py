def greet_users(names):
    """Print a simple greeting to each user in a list"""
    for name in names:
        message = f"Hello there {name.title()}"
        print(message)


users = ['jim bob', 'joe', 'jason', 'jebediah']

greet_users(users)