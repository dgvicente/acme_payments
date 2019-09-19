from answers.answer import Answer


class AnswersService:

    def __init__(self, payment_configuration, questions):
        self.payment_configuration = payment_configuration
        self.questions = questions

    def answer(self):
        return [Answer(self.payment_configuration, question) for question in self.questions]
