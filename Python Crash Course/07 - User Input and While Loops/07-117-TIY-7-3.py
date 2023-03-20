#multiples of 10

numtocheck = input("Please enter a number and I'll see if it's a multiple of 10\nINPUT: ")

numtocheck = int(numtocheck)

if numtocheck % 10 == 0:
    print("Looks like a multiple of 10")
else:
    print("Get this bullshit out of here.")