#dog

class Dog:
    """A hyper-realistic model of a dog."""

    def __init__(self, name, age):
        """Init name and age attributes"""
        self.name = name
        self.age = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulat rolling over in response to a command"""
        print(f"{self.name} rolled over.")


my_dog = Dog('Jinju', 5)

print(f"\nMy dog's name is {my_dog.name}")

print(f"My dog is {my_dog.age} years old.")

my_dog.sit()

my_dog.roll_over()


your_dog = Dog('Missy', 12)

print(f"\nYour dog's name is {your_dog.name}")

print(f"Your dog is {your_dog.age} years old.")

your_dog.sit()

your_dog.roll_over()
