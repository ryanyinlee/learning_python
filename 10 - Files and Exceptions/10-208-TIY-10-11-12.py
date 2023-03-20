#10-11 favorite number
#10-12 refactored

import json

filename = 'favenum.json'

def get_number(filename):
    """Gets the userinput of a favorite number"""
    while True:
        fave_num = input("Please input your favorite number!: ")

        numcheck = check_number(fave_num)
        
        if numcheck:
            with open(filename, 'w') as f:
                    json.dump(fave_num, f)
            return fave_num
            

def get_stored_number(filename):
    """Gets a stored number from a JSON, if any"""
    try:
        with open(filename) as f:
            fave_num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fave_num

def read_number():
    """Reads the user's favorite number"""
    fave_num = get_stored_number(filename)
    if fave_num:
        print(f"Your favorite number is {fave_num}!")
    else:
        fave_num = get_number(filename)
        print(f"Your favorite number is {fave_num}, and we shall remember it.")

def check_number(input):
    """Makes sure the user entered a number"""
    try:
        entry = int(input)
        return True
    except ValueError:
        try:
            entry = float(input)
            return True
        except ValueError:
            print(f"Please enter your favorite NUMBER: ")
            return False
    

read_number()