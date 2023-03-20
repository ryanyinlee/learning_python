"""Admin privileges module."""

class Privileges():
    """Has attributes of the privileges for an admin or user"""

    def __init__(self):
        self.privileges = ['add', 'delete', 'ban']
    
    def show_privileges(self):
        print(f"\nYou have the following privileges:")
        for privilege in self.privileges:
            print(f"{privilege.title()}")
             

