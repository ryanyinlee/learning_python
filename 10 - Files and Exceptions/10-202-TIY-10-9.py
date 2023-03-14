files = ['cats.txt', 'dogs.txt']

def openandread(filename):
    filepath = f'/Users/ryanlee/projects/python/10 - Files and Exceptions/text/{filename}'
    try:
        with open(filepath) as file_object:
            lines = file_object.readlines()

        for line in lines:
            print(line.strip())
    except FileNotFoundError:
        pass


for file in files:
    openandread(file)