

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


