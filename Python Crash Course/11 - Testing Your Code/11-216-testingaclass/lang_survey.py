from survey import Survey

question = "What is your first language?"

survey = Survey(question)

survey.show_question()

print("Enter Q to quit at any time..\n")

while True:
    response = input("Language: ")
    if response.lower() == 'q':
        break
    survey.store_response(response)