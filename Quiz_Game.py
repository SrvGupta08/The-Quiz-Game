# Quiz Game using OOPs and Classes

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:                              # Accessing the dictionaries of question_data
    text = question["text"]                                 # assigning the question of dictionaries to a local variable
    answer = question["answer"]                             # assigning the answer of that question to a local variable
    new_question = Question(text = text, answer = answer)   # creating objects for each questions
    question_bank.append(new_question)                      # putting those objects into a list

quiz = QuizBrain(question_bank)                             # Object of class QuizBrain

while quiz.still_has_questions:
    quiz.next_question()

print("You've completed the Quiz!")
print(f"You're final score is: {quiz.score}/{quiz.question_number}")