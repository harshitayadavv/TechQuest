# question.py
class Question:
    def __init__(self, question_text, options, answer):
        self.question_text = question_text
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.upper() == self.answer
