

class Question:

    def __init__(self, user_id, qn, user):
        self.user_id = user_id
        self.qtn = qn
        self.user = user
        self.answers = list() 

    """return_answers returns answers to a question"""
    def return_answers(self):
        return self.answers

    """returns user """
    def return_user(self):
        return self.user
