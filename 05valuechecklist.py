requested_toppings = ['mushrooms', 'onions', 'pineapple']

if 'mushrooms' in requested_toppings:
    print("True")
else:
    print("False")


banned_users = ['andrew', 'carolina','david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, is allowed.")