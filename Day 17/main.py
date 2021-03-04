from data import question_data_2
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data_2['results']:
    question_bank.append(Question(question['question'], question['correct_answer']))

quiz_brain_main = QuizBrain(question_bank)

quiz_brain_main.question_main()
