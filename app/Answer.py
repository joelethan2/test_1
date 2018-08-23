"""Answers details"""

class Answer:

    def __init__(self, qn_id, answer, author, voteup, votedown):
        self.qn_id=qn_id
        self.answer=answer
        self.author=author
        self.voteup=voteup
        self.votedown=votedown

    def return_qn_id(self):
        return self.qn_id

    def return_answer(self):
        return self.answer

    def return_ans_author(self):
        return self.author

    def return_votes(self):
        return self.voteup-self.votedown
