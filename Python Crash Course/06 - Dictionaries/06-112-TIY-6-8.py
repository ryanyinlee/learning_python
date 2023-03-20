#6-8 Pets

jinju = {
    'name': 'jinju',
    'species': 'puppy',
    'owner name': 'ryan',
}

beanut=  {
    'name': 'beanut',
    'species': 'borb',
    'owner name': 'ryan',
}

googoo = {
    'name': 'googoo',
    'species': 'floof',
    'owner name': 'ryan',
}

cookie = {
    'name': 'cookie',
    'species': 'birb',
    'owner name': 'mish',
}

ruby = {
    'name': 'ruby',
    'species': 'monch',
    'owner name': 'mish',
}

pets = [jinju, beanut, googoo, cookie, ruby]

for pet in pets:
    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")