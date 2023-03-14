import json


def remembering():
    """Saves a users name into a JSON to be remembered."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input('What is your name?: ')
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember your name {username.title()}.")

    else:
        print(f"We have remembered you, {username.title()}.")

remembering()