
class Answer: 

    def __init__(self, qn_id, answer, user):
        self.qn_id = qn_id
        self.answer = answer
        self.user = user

    def return_qn_id(self):
        return self.qn_id

    def return_user(self):
        return self.user

    def return_answer(self):
        return self.answer


        