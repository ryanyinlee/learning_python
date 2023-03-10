#9-5 login attempts

class User:
    """Creates a user profile with their name and information"""

    def __init__(self, first_name, last_name, age, occupation):
        """Init user's personal information"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.login_attempts = 0
    
    def describe_user(self):
        """Prints a description of the user based on information in their profile"""
        print(f"The user's name is {self.first_name.title()} {self.last_name.title()}, and they are a {self.age} year old {self.occupation}")

    def greet_user(self):
        """Prints a greeting to the user."""
        print(f"Hello there {self.first_name.title()}!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



user0 = User('Jim', 'Bob', 33, 'Plumber')

user1 = User('Miranda', 'Wang', 28, 'Architect')

user2 = User('Franklin', 'Arturo', 26, 'Philosopher')

user0.increment_login_attempts()

user0.increment_login_attempts()

user0.increment_login_attempts()

user0.increment_login_attempts()

user0.increment_login_attempts()

print(user0.login_attempts)

user0.reset_login_attempts()

print(user0.login_attempts)