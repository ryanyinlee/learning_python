#8-12 sandwiches

sandwich_ingredients = ['ham', 'cheese', 'mustard', 'mayonaise']

sandwich_ingredients1 = ['ham', 'cheese', 'mustard', 'mayonaise', 'dolphin', 'tomato']

sandwich_ingredients2 = ['ham', 'cheese']


def sandwich_maker(ingredients):
    """Accepts a list of ingredients for a sandwich and spits out a summary"""
    print(f"Your sandwich will contain the following:")

    for ingredient in ingredients:
        print(f"{ingredient.title()}")

sandwich_maker(sandwich_ingredients)

sandwich_maker(sandwich_ingredients1)

sandwich_maker(sandwich_ingredients2)