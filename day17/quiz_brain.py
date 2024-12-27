class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        actual_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {actual_question.text} (True/False): ")
        self.check_answer(user_answer, actual_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_answer, r_answer):
        if u_answer.lower() == r_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"Your current score is {self.score}/{self.question_number}")
