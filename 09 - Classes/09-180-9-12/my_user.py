import admin

new_admin = admin.Admin('Jim', 'Peperoni', 'Hacker', 33)

new_admin.describe_user()

new_admin.privileges.show_privileges()