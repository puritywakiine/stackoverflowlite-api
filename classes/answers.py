from flask import jsonify
from datetime import datetime
class Answer(object):
	"""docstring for answers"""
	current_id=0
	answers = []
	def __init__(self, owner=None, description=None):
		self.description = description
		self.owner = owner
		self.dateposted = None
	
	def create(self, question_id, owner, description):
		self.current_id += 1
		new_answer = {
			'id': self.current_id,
			'question_id': question_id,
			'description': description,
			'owner': owner,
			'dateposted': datetime.now(),
		}
		self.answers.append(new_answer)
		return new_answer

		