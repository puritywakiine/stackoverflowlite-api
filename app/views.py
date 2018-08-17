from flask import Flask,jsonify, request
from classes.questions import Questions
# from answers.answers import Answers

app = Flask(__name__)
from app import app

newQuestion = Questions()

@app.route('/questions', methods=['POST', 'GET'])
def create_and_show_questions():
    if request.method =='POST':
        title = request.form['title']
        desc = request.form['description']
        response = newQuestion.create_questions(title, desc)
        if response == 'created':
            return jsonify('message','created!')
        return "error"
    return jsonify('message',newQuestion.view_questions)

@app.route('/question/question_id', methods=['GET'])
def get_a_question(question_id):
	question=[question for question in questions if question['id']==question_id]
	if len(question)==0:
		abort(404)
	return jsonify('question','question[0]')
