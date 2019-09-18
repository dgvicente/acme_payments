import os
from definitions import ROOT_DIR
from questions.question import Question

DEFAULT_SOURCE = os.path.join(ROOT_DIR, 'static', 'questions.txt')


class QuestionsFactory:
    def __init__(self):
        pass

    @staticmethod
    def build(input_file=DEFAULT_SOURCE):
        input_file = input_file if input_file else DEFAULT_SOURCE
        my_file = open(input_file, "r")
        questions = [Question(item) for item in my_file.readlines()]
        my_file.close()
        return questions
