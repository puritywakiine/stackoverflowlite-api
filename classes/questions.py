from flask import jsonify
from datetime import datetime

class  Question(object):
	"""docstring for  Questions"""
	current_id=0
	questions = []
	def __init__(self, title=None, owner=None, description=None):
		self.title = title
		self.description = description
		self.owner = owner
		self.dateposted = None

	def create(self, title,owner, description):
		self.current_id += 1
		new_question = {
			'id':self.current_id,
            'title': title,
            'description': description,
			'owner':owner,
            'dateposted': datetime.now(),
        }
		self.questions.append(new_question)
		return jsonify(new_question)

	def all(self):
		return jsonify(self.questions)

	def view(self, id):
		return jsonify(id)
