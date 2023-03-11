from user import User
from privileges import Privileges

"""Admin module"""

class Admin(User):
    """A more advanced user with Admin powers"""

    def __init__(self, first_name, last_name, age, occupation):
        super().__init__(first_name, last_name, age, occupation)
        self.privileges = Privileges()