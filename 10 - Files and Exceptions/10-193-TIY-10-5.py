#10-5 programming poll

filepath = '/Users/ryanlee/projects/python/10 - Files and Exceptions/text/programmingpoll.txt'

survey = True

while survey:
    answer = input('Hello there programmer - Why do you like programming?')
    print(f"Please type quit to leave the survey.")
    
    if answer.lower() == 'quit':
        break
    else:
        with open(filepath, 'a') as text_to_write:
            text_to_write.write(f"\n{answer}")

        with open(filepath) as text_to_write:
            for line in text_to_write:
                print(line)