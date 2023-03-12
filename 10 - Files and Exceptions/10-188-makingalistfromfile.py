filepath = '/Users/ryanlee/projects/python/10 - Files and Exceptions/text/pi_digits.txt'

with open(filepath) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

print(lines)
