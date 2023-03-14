filename = 'realfakefile.txt'

try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
except FileNotFoundError:
    print(f"Sorry, but {filename} does not exist.")