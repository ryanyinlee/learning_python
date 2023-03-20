# un functioned code

"""unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']

completed_models = []

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for complete_model in completed_models:
    print(complete_model)"""

# un functioned code

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing designs until none are left.
    Move each to the list completed models after done.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    
def show_completed(completed_models):
    """Show all printed models"""
    print("\nThe following models have been printed:")
    for complete_model in completed_models:
        print(complete_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']

completed_models = []

print_models(unprinted_designs, completed_models)

show_completed(completed_models)