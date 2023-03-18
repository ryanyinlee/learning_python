import unittest
from survey import Survey

class TestSurvey (unittest.TestCase):
    """Test the Survey Class"""

    def test_response_storage_single(self):
        """Test that one response is stored properly."""
        question = 'What language did you first learn?'
        survey = Survey(question)
        survey.store_response('Javascript')
        self.assertIn('Javascript', survey.responses)

    def test_response_multi(self):
        """Test that several responses are stored properly."""
        question = 'What language did you first learn?'
        survey = Survey(question)
        responses = ['Javascript', 'C#', 'Python', 'Javascript']
        for response in responses:
            survey.store_response(response)
        for response in responses:
            self.assertIn(response, survey.responses)


if __name__ == '__main__':
    unittest.main()