# main.py
from questions_data import questions
from quiz import Quiz

def main():
    print("Initializing the quiz...")
    quiz = Quiz(questions)  # Pass the questions to the Quiz
    quiz.start_quiz()  # Start the quiz

if __name__ == "__main__":
    main()
