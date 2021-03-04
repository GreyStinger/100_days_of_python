class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_input, c_question):
        if u_input != c_question.answer:
            print('Oh no, You got it wrong!')
        else:
            print('Yay, you got it right!')
            self.score += 1

    def question_main(self):
        while self.still_has_questions():
            c_question = self.question_list[self.question_number]
            user_input = str(input(
                f"Q.{self.question_number + 1} {c_question.text} (True/False)?: ").lower().capitalize())

            self.check_answer(user_input, c_question)

            print(f'It was \'{c_question.answer}\'')
            self.question_number += 1
            print(f'You have {self.score}/{self.question_number} correct.\n')
        print(f'You\'ve completed the quiz. \nYour final score was {self.score} out of {self.question_number}')
