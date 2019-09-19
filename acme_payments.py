from answers.answers_service import AnswersService
from payments_configuration.configuration_factory import ConfigurationFactory
from questions.questions_factory import QuestionsFactory


def main():
    greet()
    payments_configuration = ConfigurationFactory.build(get_config_file())
    questions = get_questions()
    give_answers(payments_configuration, questions)


def give_answers(payments_configuration, questions):
    answer_service = AnswersService(payments_configuration, questions)
    print('The answers you were looking for:')
    print('---------------------------------')
    [print(answer) for answer in answer_service.answer()]


def greet():
    print('Welcome to the ACME payments platform!')
    print('--------------------------------------')


def get_questions():
    questions = input("Now, please provide your questions file or leave it blank to use default: ")
    return QuestionsFactory.build(questions)


def get_config_file():
    config_file = input("Please provide a file path for payment rates by hour or leave it blank to use default: ")
    config_file = config_file if config_file else None
    return config_file


if __name__ == "__main__":
    main()
