import unittest
from survey import Survey

class TestSurvey (unittest.TestCase):
    """Test the Survey Class"""
    
    def setUp(self):
        """Creates the test survey and responses to test against."""
        question = 'What programming language did you first learn?'
        self.survey = Survey(question)
        self.responses = ['Javascript', 'C#', 'Python', 'Javascript']

    def test_response_storage_single(self):
        """Test that one response is stored properly."""
        self.survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.survey.responses)

    def test_response_multi(self):
        """Test that several responses are stored properly."""
        for response in self.responses:
            self.survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.survey.responses)

if __name__ == '__main__':
    unittest.main()