import json

filename = 'username.json'


def get_stored_username(filename):
    """Get a stored username from memory"""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else: 
        return username
    

def get_new_username():
    """Prompt for new username"""
    username = input('What is your name?: ')
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We shall now remember you {username.title()}")
    return username


def greet_user():
    """Remembers the user and writes them a message."""
    username = get_stored_username(filename)
    
    if username:
        print(f"We remember you, {username.title()}")
    else:
        username = get_new_username()
        
greet_user()