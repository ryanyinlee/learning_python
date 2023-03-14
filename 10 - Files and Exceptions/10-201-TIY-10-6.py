#10-6 addition

def valueAdd():
    print(f"Please enter two numbers so we can dd them.")
    
    try:
            entry0 = input('First number:')
            entry1 = input('Second number:') 

            answer = int(entry0) + int(entry1)

            print(f"Your combined total is: {answer}")
    except ValueError:
        print(f"One or more of your numbers wasn't!")

valueAdd()