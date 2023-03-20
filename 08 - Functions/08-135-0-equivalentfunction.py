def describe_pet(pet_name, animal_type="dog"):
    """Display pet information"""
    print(f"\nMy pet is a {animal_type}")
    print(f"\nMy {animal_type}'s name is {pet_name}")

describe_pet('beanut')

describe_pet(pet_name='beanut')

describe_pet('harry', 'hamster')

describe_pet(pet_name='harry', animal_type='hamster')

describe_pet(animal_type='hamster', pet_name='harry')