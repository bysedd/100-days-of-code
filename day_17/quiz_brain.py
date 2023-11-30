from question_model import Question


class QuizBrain:
    def __init__(self, question_list: list[Question]):
        self.question_number = 0
        self.question_list = question_list
        self.__score = 0

    def next_question(self) -> None:
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer: str, answer: str) -> None:
        if user_answer.strip().title() == answer:
            print("You got it right!")
            self.__score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {answer}.")
        print(f"Your current score is: {self.__score}/{self.question_number}", end="\n\n")

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)
