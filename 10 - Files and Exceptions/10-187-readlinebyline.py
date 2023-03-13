filepath = '/Users/ryanlee/projects/python/10 - Files and Exceptions/text/pi_digits.txt'

with open(filepath) as file_object:
    for line in file_object:
        print(line.rstrip())

