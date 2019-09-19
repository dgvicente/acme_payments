class Answer:
    def __init__(self, payment_configuration, question):
        self._payment_configuration = payment_configuration
        self._question = question
        self.name = self._question.name
        self.__calculate_amount_to_pay()

    def __calculate_amount_to_pay(self):
        self.amount = 0
        for question_hour_item in self._question.items:
            question_item_hours_with_rate = self._payment_configuration.get_hours_for(question_hour_item)
            for question_item_hour_with_rate in question_item_hours_with_rate:
                self.amount = self.amount + question_item_hour_with_rate['rate'] * question_item_hour_with_rate['hours']

    def __str__(self):
        return 'The amount to pay %s is: %s USD' % (self.name, self._get_as_int_if_no_decimal_points())

    def _get_as_int_if_no_decimal_points(self):
        return int(self.amount) if abs(self.amount) == abs(int(self.amount)) else self.amount
