from flask import Flask,jsonify, request, make_response
from classes.questions import Question
from datetime import datetime
from classes.answers import Answer
from flask_httpauth import HTTPBasicAuth
from classes.users import User

app = Flask(__name__, static_url_path = "")
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'purity':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify( { 'error': 'Unauthorized access' } ), 403)
    # return 403 instead of 401 to prevent browsers from displaying the default auth dialog


app = Flask(__name__)
from app import app

question = Question()
answer = Answer()
user= User()

@app.route('/auth/signup',methods=['POST'])
def signup():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    user.create(username, email, password)
    return jsonify({'message': 'Signed up successfully.'})

@app.route('/questions', methods=['POST', 'GET'])
def create_and_show_questions():
    if request.method =='POST':
        title = request.json['title']
        desc = request.json['description']
        owner = request.json['email']
        response = question.create(title, owner, desc)
        return response

    return question.all()

@app.route('/questions/<question_id>', methods=['GET'])
def view_specific_question(question_id):
    return question.view(question_id)

@app.route('/questions/<question_id>/answers', methods=['POST'])
def add_an_answer_to_a_question(question_id):
    if request.method =='POST':
        desc = request.json['description']
        owner = request.json['owner']
        response = answer.create(question_id, owner, desc)
        return jsonify(response)
