#9-7 admin

class User:
    """Creates a user profile with their name and information"""

    def __init__(self, first_name, last_name, age, occupation):
        """Init user's personal information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
    
    def describe_user(self):
        """Prints a description of the user based on information in their profile"""
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}, and they are a {self.age} year old {self.occupation}")

    def greet_user(self):
        """Prints a greeting to the user."""
        print(f"Hello there {self.first_name.title()}!")

class Admin(User):
    """A more advanced user with Admin powers"""

    def __init__(self, first_name, last_name, age, occupation):
        super().__init__(first_name, last_name, age, occupation)
        self.privileges = ['add', 'delete', 'ban']

    def show_privileges(self):
        print(f"\n{self.first_name} {self.last_name} has the following privileges:")
        for privilege in self.privileges:
            print(f"{privilege.title()}")
            

user0 = User('Jim', 'Bob', 33, 'Plumber')

admin1 = Admin('Jim', 'Bob', 33, 'Plumber')

admin1.show_privileges()