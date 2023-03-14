filename = '/Users/ryanlee/projects/python/10 - Files and Exceptions/text/realfakefile.txt'


try:
    with open(filename, encoding='utf-8') as file:
        contents = file.read()
except FileNotFoundError:
    print(f"Sorry, but {filename} does not exist.")
else:
    words = contents.split()
    numwords = len(words)
    print(f"File {filename} has {numwords} words.")



