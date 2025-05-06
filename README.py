# 📝 Project: Quiz Grader

#### 🎥 Video Demo: [Insert Your Demo URL Here]

---

## 📖 Description

**Quiz Grader** is a command-line Python application that tests a user’s knowledge by presenting them with a set of 10 multiple-choice or short-answer questions from a CSV file, capturing their responses, and calculating a final score as a percentage. This project simulates a lightweight and interactive quiz system that could be adapted for learning assessments, exam preparation, or casual knowledge testing.

Upon execution, the user is greeted with instructions and presented with each question sequentially. After answering all questions, the program automatically grades the answers by comparing them with the correct answers from the file and outputs the user’s score in percentage format.

This project is written entirely in Python, uses only built-in libraries (primarily `csv` for file handling), and follows a modular structure to promote readability and testability.

---

## 🗂️ Files in the Project

### `project.py`
This is the core program that drives the quiz system. It includes the following functions:

- **`main()`**  
  Serves as the entry point of the application. Handles the user interface, question loading, grading, and displaying results.

- **`load_questions()`**  
  Loads the questions and answers from `questions.csv` using Python’s built-in `csv.DictReader`.

- **`ask_questions()`**  
  Prompts the user to answer each question. Collects and returns responses.

- **`load_answers()`**  
  Extracts correct answers from the loaded question list.

- **`auto_grader()`**  
  Compares user responses to correct answers and calculates the score.

- **`get_percentage()`**  
  Converts the numeric score into a percentage.

---

### `questions.csv`
A CSV file that contains the quiz data. Each row includes:
- `question`: The text of the question.
- `answer`: The correct answer.

This file is read by the program and can be updated easily without modifying code.

---

### `test_project.py`
This file contains unit tests written using `pytest` to verify key functions. It ensures the program is reliable and easy to maintain.

Tested functions include:

- ✅ `load_questions()`
- ✅ `load_answers()`
- ✅ `auto_grader()`
- ✅ `get_percentage()`

---

## ⚖️ Design Decisions

- **CSV File Format**  
  Chosen for its simplicity and ease of manual editing or generation from spreadsheets.

- **Function Modularization**  
  Each component has its own function, making it easier to test and modify independently.

- **Testing Strategy**  
  Focused on pure functions like grading and answer loading to ensure correctness without depending on user input.

- **User Interface**  
  Simple command-line prompts guide the user clearly through the quiz process.

---

## ✅ How to Run

To execute the quiz:

```bash
python project.py
