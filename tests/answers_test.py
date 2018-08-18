import unittest
import json
 
Class stackoverflow_apiTestCase(unnitest.TestCase)
     """This class represents the stackoverflow_api testcase"""


    def setUp(self):
    	"""Define test variables and initialize the app."""
    	self.app=create_app(config_name="testing")
    	self.client=self.app.test_client
    	self.stackoverflow_api={"questions": "questions"}


    def test_stackoverflow_api_can_add_an_answer_to_a_question(self):
        """Test API can create an answer to a question (POST answer)"""
        res = self.client().post('/stackoverflow_api/', data=self.stackoverflow_api)
        self.assertEqual(res.status_code, 201)
        self.assertIn('What is flask?', str(res.data))
