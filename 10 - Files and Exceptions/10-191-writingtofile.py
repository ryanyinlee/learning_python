filepathtotext = '/Users/ryanlee/projects/python/10 - Files and Exceptions/text/programming.txt'

with open(filepathtotext, 'w') as text_obj:
    text_obj.write('Hello text file world.')
    text_obj.write("\nThis is a new line.")
    text_obj.write("\nThis is a new line #2.")