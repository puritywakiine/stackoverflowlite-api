class  Questions(object):
	"""docstring for  Questions"""
	questions = []
	def __init__(self, title=None, description=None):
		self.title = title
		self.description = description

	def create_questions(self, title, description):
		new_question = [title, description]
		self.questions.append(new_question)
		return "created"

	def view_questions(self):

		return self.questions
