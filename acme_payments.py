from configuration_factory.configuration_factory import ConfigurationFactory


def main():
    greet()
    payments_configuration = ConfigurationFactory.build(get_config_file())
    questions = get_questions()
    give_answers()


def give_answers():
    print('The answers you were looking for:')
    print('---------------------------------')
    print('The amount to pay RENE is: 215 USD')


def greet():
    print('Welcome to the ACME payments platform!')
    print('--------------------------------------')


def get_questions():
    questions = input("Now, please provide your questions file or leave it blank to use default: ")
    return questions if questions else None


def get_config_file():
    config_file = input("Please provide a file path for payment rates by hour or leave it blank to use default: ")
    config_file = config_file if config_file else None
    return config_file


if __name__ == "__main__":
    main()
