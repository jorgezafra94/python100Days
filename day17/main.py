from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for x in question_data:
    q = Question(**x)
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your score is {quiz.score}/{quiz.question_number}")