

from flask import Flask, jsonify, request,Response, json
from flask_api import FlaskAPI

# local import
from instance.config import app_config

config_name = "development"

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    
    
    @app.route('/')
    def hello_world():
        return 'Welcome to challenge_2'

    ### GET all questions#
    @app.route('/questionz')
    def get_questions():
        return jsonify({'questions': questions})

    ### GET a question/qnid_number#
    @app.route('/questionz/<int:qn_id>')
    def get_a_question(qn_id):
        question={}
        for item in questions:
            if qn_id==item['qn_id']:
                question={
                    'qn_id':item['qn_id'],
                    'qn':item['qn'],
                    'aurthor':item['aurthor'],
                    'answer':item['answer'],
                }
        return jsonify(question)

    ###POST a question#
    @app.route('/questionz', methods=['POST'])
    def add_question():
        request_data = request.get_json()
        if (valid_question(request_data)):
            question={
                'qn_id':request_data['qn_id'],
                'qn':request_data['qn'],
                'aurthor':request_data['aurthor'],
                'answer':request_data['answer']
            }
            questions.append(question)
            return jsonify(question)
        else:
            bad_object={
                "error":"Invalid question object",
                "help_string":
                    "Request format should be "
                    "{'qn_id':001,'qn':'what?','aurthor':'jack'}"
            }
            response = Response(json.dumps(bad_object), status=400, mimetype="application/json")
            return response


    ###POST an answer
    @app.route('/questionz/<int:qn_id>/answers', methods=['POST'])
    def add_ans(qn_id):

        request_ans = request.json
        for item in questions:
            if (item['qn_id'] == qn_id ):
                yr=item
                ans = {
                'ans_id': request_ans['ans_id'],
                'answer': request_ans['answer'],
                'aurthor': request_ans['aurthor'],
                'votedown': request_ans['votedown'],
                'voteup': request_ans['voteup']
                }

                questions[questions.index(yr)]['answer'].append(ans)
                return jsonify(ans)




    def valid_question(questionObject):
        if "qn" in questionObject and "aurthor" in questionObject and "qn_id" in questionObject:
            return True
        else:
            return False

    questions=[
        {
            'qn_id':122,
            'qn':'what is your name?',
            'aurthor':'joel',
            'answer':[
                    ]
        },
        {
            'qn_id':123,
            'qn':'what is your name?',
            'aurthor':'joel',
            'answer':[
                    {'ans_id':123,'answer':'My name is joel.','aurthor':'joel','voteup':12,'votedown':5},
                    {'ans_id':124,'answer':'My name is simon.','aurthor':'simon','voteup':12,'votedown':5}
                    ]
        },
        {
            'qn_id':124,
            'qn':'How old are you?',
            'aurthor':'ian',
            'answer':[
                    {'ans_id':123,'answer':'Am 20 years old.','aurthor':'simon','voteup':12,'votedown':5},
                    {'ans_id':124,'answer':'Am 5 years old.','aurthor':'joellah','voteup':12,'votedown':5}
                    ]
        },
        {
            'qn_id':125,
            'qn':'what is your sex?',
            'aurthor':'ethan',
            'answer':[
                    {'ans_id':123,'answer':'I am a male','aurthor':'simon','voteup':12,'votedown':5},
                    {'ans_id':124,'answer':'I am a female.','aurthor':'viola','voteup':12,'votedown':5}
                    ]
        }
    ]

    return app