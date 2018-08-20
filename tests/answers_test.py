import unittest
import json
 
class StackoverflowapiTestCase(unnitest.TestCase):
     """This class represents the stackoverflow_api testcase"""

    def setUp(self):
     	"""Define test variables and initialize the app."""
    	self.client=app.test_client(self)
    	self.answer={"answer": "answer"}
        self.user = {'email':'pur@gmail.com', 'username':'pure', 'password':'123qwertds', }
        create_user = self.client.post('/auth/signup', self.data = self.user)
    
    def test_it_creates_an_answer_to_a_question(self):
        new_answer = {'question_id': 1, 'description': 'A description','owner': 'owner','dateposted': 'datetime.now()'}
        response = self.client.post('/answers', data=new_answer)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertDictContainsSubset(new_answer, json.loads(response.data)['answer'])

    