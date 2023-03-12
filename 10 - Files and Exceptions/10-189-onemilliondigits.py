filepath = '/Users/ryanlee/projects/python/10 - Files and Exceptions/text/pi_onemil.txt'

with open(filepath) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday in the form MMDDYY: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday is not in the first million digits of pi.")