
from flask import Flask, request, jsonify
from app.Question import Question
from app.Answer import Answer
from app.Storage import Store

app = Flask(__name__)
store = Store()


@app.route('/')
def index():
	return '<h1 style="text-align:center;">Welcome to challenge_2</h1>'
	
	
#POST a question
@app.route('/v1/questions', methods=['POST'])
def add_a_questions():

    if not request.form['user']:
        response = jsonify( {'error': 'User field  is empty'} )
        response.status_code = 400
        return response

    if not request.form['qn']:
        response = jsonify( {'error': 'Question field is empty'} )
        response.status_code = 400
        return response

    new_qn = Question(2, request.form['qn'], request.form['user'])
    response = jsonify(store.add_question(new_qn))
    response.status_code = 201
    return response




#GET all questions
@app.route('/v1/questions')
def get_questions():

    output = store.return_questions()
    response = jsonify(output)
    response.status_code = 200
    return response


#GET a question
@app.route('/v1/questions/<int:qn_id>/')
def get_a_question(qn_id):
   
    if store.return_a_question(qn_id) :
        response = jsonify(store.return_a_question(qn_id))
        response.status_code = 200
        return response

    output = { 'error':  request.url+ ':- has no Question.' }
    response = jsonify(output)
    response.status_code = 404
    return response


#add answer to question
@app.route('/v1/questions/<int:qn_id>/answers', methods=['POST'])
def answer_a_question(qn_id):
    if not request.form['user'] :
        response = jsonify({'error': 'User field  is empty'})
        response.status_code = 400
        return response
        
    if  not request.form['answer']:
        response = jsonify({'error': 'Answer field is empty'})
        response.status_code = 400
        return response


    new_ans = Answer(qn_id, request.form['answer'], request.form['user'])
    store_resp=store.add_answer(new_ans)
    if  store_resp:
        response = jsonify(store_resp)
        response.status_code = 200
        return response

    response = jsonify({ 'error':  request.url+ ': has no Question.' })
    response.status_code = 404
    return response



