# A program that reads a CSV file containing questions and answers, asks the user to answer the questions, and grades the answers.
# Required Libraries
import csv

def main():
    """Main function to run the quiz program."""
    print("Welcome to the quiz program!")
    print("You will be asked 10 questions.")
    questions = load_questions()
    answers = ask_questions(questions)
    correct_answers = load_answers(questions)
    grade = auto_grader(answers, correct_answers)
    percentage = get_percentage(grade)
    print(f"Score:  {percentage:.0f}%")


def load_questions():
    """Load questions from a CSV file."""
    with open("questions.csv", "r", newline="") as ques_file:
        reader = csv.DictReader(ques_file)
        questions = []
        for row in reader:
            questions.append(row)
    return questions


def ask_questions(questions):
    """Ask the user questions and return their answers as a list."""
    print("Please answer the following questions:")
    print("Type your answer and press Enter.")
    answers = []
    for question in questions:
        answers.append(input(f"{question['question']} "))
    return answers

def load_answers(questions):
    """
    Load the correct answers from the questions which is a list
    of dictionaries with questions and answers.
    """
    correct_answers = []
    for question in questions:
        correct_answers.append(question["answer"])
    return correct_answers

def auto_grader(ans, corr_ans):
    """
    Compare the user's answers with the correct answers and return the score.
    The score is the number of correct answers.
    """
    score = 0
    for  i in range(10):
        if ans[i] == corr_ans[i]:
            score += 1
    return score

def get_percentage(grade):
    """
    Convert the score to a percentage.
    The percentage is the score divided by the total number of questions (10).
    """
    return round(grade / 10, 1) * 100


if __name__ == "__main__":
    main()