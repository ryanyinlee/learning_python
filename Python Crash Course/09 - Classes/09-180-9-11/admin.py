import user


user0 = user.User('Jim', 'Bob', 33, 'Plumber')

admin1 = user.Admin('Jim', 'Bob', 33, 'Plumber')

admin1.privileges.show_privileges()