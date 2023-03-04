fave_langs = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}


people_to_survey = {
    "jen",
    "bill",
    "linus",
    "sarah",
    "edward",
    "phil",
}

for name in people_to_survey:
    if name in fave_langs.keys():
        print(f"\nDearest {name.title()}, thank you for taking our survey :))))")
    else:
        print(f"\n{name.title()}. First of all: How dare you? \n Second: Please take our survey.")