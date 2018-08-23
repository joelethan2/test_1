

from datetime import datetime
import Answer

"""Question details"""

class Question:

    def __init__(self, qn, qn_id, author):
        self.qn_id=qn_id
        self.qn=qn
        self.author=author
        self.answers=list()

    def return_answers(self):
        return self.answers

    def return_qn_author(self):
        return self.author


# dictionary to store all questions
questions={}

def add_Questiion(new_qn):
    if isinstance(new_qn, Question):
        qns_pos=len(questions) + 1
        questions[qns_pos]=new_qn.__dict__
        return questions[qns_pos]
    raise TypeError('Invalid Question, please try again')

def return_questions():
    return questions

def return_a_question(qn_id):
    if qn_id in questions:
        return questions[qn_id]

def add_an_answer(new_ans):
    if not isinstance(new_ans, Answer):
        TypeError('Please enter a valid answer')

    if new_ans.qn_id in questions:
        question = questions[new_ans.qn_id]
        question['answer'].append(new_ans)
        return  questions[new_ans.qn_id]