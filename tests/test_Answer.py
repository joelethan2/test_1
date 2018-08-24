
from app.Answer import Answer


def test_is_instance_of_Answer_class():
    new_answer = Answer(4, "Yess!", "Mwebaze")
    assert isinstance(new_answer, Answer)

def test_has_qn_id():
    new_answer = Answer(3, "Python is.....", "Ethan")
    assert hasattr(new_answer, "qn_id")

def test_has_user():
    new_answer = Answer(2, "answer", "Joel")
    assert hasattr(new_answer, "user")



