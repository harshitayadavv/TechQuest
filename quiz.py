# quiz.py
from question import Question
import time
from utils import Timer

class Quiz:
    def __init__(self, questions):
        self.questions = [Question(q["question"], q["options"], q["answer"]) for q in questions]
        self.score = 0
        print(f"Loaded {len(self.questions)} questions.")

    def start_quiz(self):
        timer = Timer(60)  # 60 seconds timer
        timer.start()

        for question in self.questions:
            if timer.time_left <= 0:
                print("Time's up! Quiz ended.")
                break

            print(f"Question: {question.question_text}")  # Display the question
            for option in question.options:  # Display the options
                print(option)

            user_answer = input("Enter your answer (A/B/C/D): ")
            if question.check_answer(user_answer):
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question.answer}\n")

        print(f"Quiz finished! Your score is {self.score}/{len(self.questions)}.")
