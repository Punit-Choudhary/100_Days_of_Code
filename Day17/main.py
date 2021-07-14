from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    question_bank.append(Question(data['text'], data['answer']))

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed this quiz 🎈")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
