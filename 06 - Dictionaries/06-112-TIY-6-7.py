#6-7 People

mishmoosh = {
    'first name': 'mish',
    'last name': 'moosh',
    'age': 36,
    'city': 'sunnyside',
    }

bebe = {
    'first name': 'meara',
    'last name': 'lee',
    'age': 0.9,
    'city': 'edmonds',
    }

jinju = {
    'first name': 'jin',
    'last name': 'ju',
    'age': 4,
    'city': 'seoul',
    }

people = [mishmoosh, bebe, jinju]

for person in people:
    for key, value in person.items():
        if type(value) == str:
            print(f"{key.title()}: {value.title()}")
        elif type(value) == float or type(value) == int:
            print(f"{key.title()}: {value}")