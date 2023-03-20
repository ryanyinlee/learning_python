

def countwords(filename):
    filepath = f'/Users/ryanlee/projects/python/10 - Files and Exceptions/text/{filename}'
    try:
        with open(filepath, encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        numwords = len(words)
        print(f"File {filename} has {numwords} words.")

"""filename = '/Users/ryanlee/projects/python/10 - Files and Exceptions/text/realfakefile.txt'

countwords(filename)


"""

filenames = ['realfakefile.txt', 'realfakefile100.txt','realfakefile2.txt','realfakefile3.txt', 'realfakefile1.txt']

for filename in filenames:
    countwords(filename)