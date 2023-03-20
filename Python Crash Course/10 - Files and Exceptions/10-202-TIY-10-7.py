#10-7 addition calculator

def valueAdd():
    print(f"Please enter two numbers so we can dd them.")
    print("Enter Q to quit.")
    while True:
        try:
                entry0 = input('First number:')
                if entry0 == 'q':
                    break
                entry1 = input('Second number:') 
                if entry1 == 'q':
                    break
                
                answer = int(entry0) + int(entry1)

                print(f"Your combined total is: {answer}")
        except ValueError:
            print(f"One or more of your numbers wasn't!")

valueAdd()