favorite_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_lang.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("These lang have been mentioned")
for lang in set(favorite_lang.values()):
    print(lang.title())