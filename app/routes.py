
from flask import Flask, jsonify, request,Response, json
from flask_api import FlaskAPI
from app.Answer import Answer
from app.Question import Question
from app.Storage import Store

from instance.config import app_config

config_name = "development"

app = FlaskAPI(__name__)
store = Store()

@app.route('/')
def hello_world():
    return 'Welcome to challenge_2'

#Post a question
@app.route('/questions', methods=['POST'])
def add_question():
    if request.form['author']:
        if request.form['qn']:
            new_qn=Question(2, request.form['qn'], request.form['author'])
            response = jsonify(store.add_a_questiion(new_qn))
            response.status_code=201
            return response

        response = jsonify({'error':'Question field not entered'})
        response.status_code = 400
        return response

    response = jsonify({'error':'Author field not entered'})
    response.status_code = 400
    return response

@app.route('/questions')
def get_questions():
    response = jsonify(store.get_all_questions())
    response.status_code=200
    return response

@app.route('/questions/<int:qn_id>')
def get_a_question(qn_id):
    if store.return_a_question(qn_id):
        response = jsonify(store.return_a_question(qn_id))
        response.status_code=200
        return response

    response = jsonify({'error':'Question not found'})
    response.status_code=404
    return response
