# This is a test file for the project module.
# Rquired Libraries
from project import load_answers, auto_grader, get_percentage, load_questions


correct_answers = ["def", "bool", "#", "input", "for", "dictionary", "try", "len", "pass", "tuple"]
answers = ["def", "bool", "#", "input", "for", "dictionary", "try", "tuple", "pass", "len"]


def test_load_questions():
    """Test the load_questions function to ensure it returns the correct questions."""
    questions = load_questions()
    assert len(questions) == 10
    assert type(questions) == list
    assert type(questions[0]) == dict

def test_load_answers():
    """Test the load_answers function to ensure it returns the correct answers."""
    questions = load_questions()
    assert load_answers(questions) == correct_answers

def test_auto_grader(ans=answers, corr_ans=correct_answers):
    """Test the auto_grader function to ensure it returns the correct score."""
    assert auto_grader(answers, correct_answers) == 8

def test_get_percentage(grade=8):
    """Test the get_percentage function to ensure it returns the correct percentage."""
    assert get_percentage(grade) == 80.0