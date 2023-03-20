#10-2 learning C

filepath = '/Users/ryanlee/projects/python/10 - Files and Exceptions/text/learningpython.txt'

with open(filepath) as file_object:
    for line in file_object:
        line = line.replace('Python', 'C')
        print(line.rstrip())

