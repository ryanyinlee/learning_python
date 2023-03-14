print("Please enter two numbers so I can divide them.")
print("Enter Q t quit.")

while True:
    first_number = input(f'\nFirst Number:')
    if first_number.lower() == 'q':
        break
    second_number = input(f'\nSecond Number:')
    if second_number.lower() == 'q':
        break
    try:
        answer = int(first_number) / int(second_number) 
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)