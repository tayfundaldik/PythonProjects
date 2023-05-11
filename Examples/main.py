from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

n = 0
for n  in range (0,len(question_data)):

    question_bank.append(Question(question_data[n]["text"],question_data[n]["answer"]))

quiz=QuizBrain(question_bank)
quiz.next_question()
cont=True
while quiz.still_has_questions():
    quiz.next_question()
    print("You completed the quiz.")
    print(f"Your score {quiz.count}/{quiz.question_number}")