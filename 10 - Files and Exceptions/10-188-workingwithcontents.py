filepath = '/Users/ryanlee/projects/python/10 - Files and Exceptions/text/pi_digits.txt'

with open(filepath) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)

print(len(pi_string))