def readThe(filename):

    with open(filename) as fileobject:
        contents = fileobject.read()
        thecount = contents.lower().count('the ')
        print(f"The file you analyzed had the word 'the' in it {thecount} times.")
    

readThe('/Users/ryanlee/projects/python/10 - Files and Exceptions/text/gutenberg1.txt')



"""        words = contents.split()
        thecount = 0
        for word in words:
            if word.lower() == 'the':
                thecount += 1"""