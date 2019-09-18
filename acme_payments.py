def main():
    print 'Welcome to the ACME payments platform!'
    print '--------------------------------------'
    config_file = raw_input("Please provide a file path for payment rates by hour or leave it blank to use default: ")
    print config_file if config_file else 'DEFAULT'
    questions = raw_input("Now, please provide your questions file or leave it blank to use default: ")
    print questions if questions else 'DEFAULT'
    print 'The answers you were looking for:'
    print '---------------------------------'
    print 'The amount to pay RENE is: 215 USD'


if __name__ == "__main__":
    main()
