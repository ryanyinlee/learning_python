filepathtotext = '/Users/ryanlee/projects/python/10 - Files and Exceptions/text/appendprogramming.txt'

with open(filepathtotext, 'a') as text_obj:
    text_obj.write('\nHello text file world.')
    text_obj.write("\nThis is a new line.")
    text_obj.write("\nThis is a new line #2.")