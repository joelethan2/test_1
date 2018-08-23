
from app.Question import Question
from app.Answer import  Answer

class Store:
    def __init__(self):
        self.qns=[]

    def get_all_questions(self):
        return self.qns


    def add_a_questiion(self, new_qn):
        if isinstance(new_qn, Question):
            qns_pos=len(self.qns) + 1
            self.qns[qns_pos]=new_qn
            return self.qns[qns_pos]
        raise TypeError('Invalid Question, please try again')




    def return_a_question(self, qn_id):
        if qn_id in self.qns:
            return self.qns[qn_id]


    
    def add_an_answer(self, new_ans):
        if isinstance(new_ans, Answer):
            if new_ans.qn_id in self.qns:
                question = self.qns[new_ans.qn_id]
                question['answer'].append(new_ans)
                return  self.qns[new_ans.qn_id]

        raise TypeError('Please enter a valid answer')

    