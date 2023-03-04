user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nthe key be: {key}")
    print(f"the value be: {value}")

favorite_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_lang.items():
    print(f"\n{name.title()}'s fave lang is {language.title()}")

for name in favorite_lang.keys():
    print(f"Name: {name.title()}")

for name in favorite_lang:
    print({name})

friends = ['phil','sarah']

for name in favorite_lang.keys():
    print(f"hi {name}")

    if name in friends:
        language = favorite_lang[name]
        print(f"\t{name}, I see you like {language}")

if 'erin' not in favorite_lang.keys():
    print('Erin, pls poll, pls')

