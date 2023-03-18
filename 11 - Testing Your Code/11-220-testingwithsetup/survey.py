class Survey:
    """Collect answers to a survey"""

    def __init__(self, question):
        """Store a question, then prepare to store response"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the question"""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """Show responses to survey"""
        print("The survey results are: ")
        for response in self.responses:
            print(f"{response}")