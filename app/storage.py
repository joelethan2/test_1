

from app.Answer import Answer
from app.Question import Question

class Store:
    def __init__(self):
        self.questions = {}
    
    def return_questions(self):
        return self.questions

    def add_question(self, new_qn):
        if isinstance(new_qn, Question):
            qn_id = len(self.questions) + 1
            self.questions[qn_id] = new_qn.__dict__
            return self.questions[qn_id]
        raise TypeError(str(new_qn) +' not an instance of Question')

    #method to return a single question.
    def return_a_question(self, qn_id):
        if qn_id in self.questions:
            return self.questions[qn_id]

    #add answer
    def add_answer(self, new_ans):
        if not isinstance(new_ans, Answer):
            raise TypeError(str(new_ans) + ' not an instance of Answer')

        if new_ans.qn_id in self.questions:
            question = self.questions[new_ans.qn_id]
            question['answers'].append(new_ans.__dict__)
            return self.questions[new_ans.qn_id]



