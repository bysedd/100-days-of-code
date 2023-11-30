from typing import Literal

ANSWER = Literal["True", "False"]


class Question:
    def __init__(self, text: str, answer: ANSWER):
        self.text = text
        self.answer = answer
