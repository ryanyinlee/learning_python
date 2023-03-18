class Employee:
    """Model of an employee"""

    def __init__(self, first, last, salary):
        """Create model with first and last name and salary"""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self):
        """Gives a raise to the employee"""
        self.salary = 5000 + self.salary
        return self.salary
    
    def give_custom_raise(self, amount):
        """Gives a raise to the employee"""
        self.salary = amount + self.salary
        return self.salary
    

test_employee0 = Employee('Jim', 'Bobly', 50_000)

print(test_employee0)