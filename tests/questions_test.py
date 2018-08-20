import json
import unittest
from app import app



class questionApiTestCase(unittest.TestCase):

    def setUp(self):
    	"""Define test variables and initialize the app."""
    	self.client=app.test_client(self)
    	self.questions={"questions": "questions"}
        self.user = {'email':'pur@gmail.com', 'username':'pure', 'password':'123qwertds', }
        create_user = self.client.post('/auth/signup', self.data = self.user)
        
    def test_it_shows_all_questions(self):
        response = self.client.get('/questions')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertEqual(json.loads(response.data), {
            'questions': self.questions, 'count': len(self.questions)
        })

    def test_it_gets_a_specific_questions(self):
        response = self.client.get('/questions/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.mimetype, 'application/json')
        # The first index of questions has id == 1
        self.assertEqual(json.loads(response.data), {'question': self.questions[3]})

    def test_it_creates_new_questions(self):
        new_question = {'id': 1, 'title': 'A title',, 'description': 'A description',, 'owner': 'owner',, 'dateposted': 'datetime.now()'}
        response = self.client.post('/questions', data=new_question)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.mimetype, 'application/json')
        self.assertDictContainsSubset(new_question, json.loads(response.data)['question'])
