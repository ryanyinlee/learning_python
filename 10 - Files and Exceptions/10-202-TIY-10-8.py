files = ['10 - Files and Exceptions/cats.txt', '10 - Files and Exceptions/dogs.txt']

def openandread(filename):
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()

        for line in lines:
            print(line.strip())
    except FileNotFoundError:
        print(f"File {filename} could not be found.")


for file in files:
    openandread(file)