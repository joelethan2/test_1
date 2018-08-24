from app.Question import Question


def test_is_instance_of_Question_class():
    new_qtn = Question(6, "What?", "Arthur")
    assert isinstance(new_qtn, Question)

def test_has_user_id():
    new_qtn = Question(10, "Who?", "Simon")
    assert hasattr(new_qtn, "user_id")

def test_has_user():
    new_qtn = Question(3, "Where?", "Ethan")
    assert hasattr(new_qtn, "user")
