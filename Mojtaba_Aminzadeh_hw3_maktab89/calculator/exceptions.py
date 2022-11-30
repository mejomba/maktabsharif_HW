import sys
from logic.parse import parser
from logic.calc import calculator


invalid_format = 'Invalid Format Exception'


def help_user():
    print(f'calculator for {{ + - * / }} operation\n'
          f'valid format input: {{number}} {{operator}} {{number}}\n'
          f'type "exit" for close program\n{40 * "-"}\n')


def logger(*args):
    user_input, result = args
    with open('history.txt', 'a') as log_file:
        log_file.write(f'{user_input} = {result}\n')


def exception_logger(user_input, error):
    print(f'> {error}\n')
    help_user()
    logger(user_input, error)


def run():
    try:
        user_input = input('> ')
        if user_input == 'exit':
            logger(user_input, 'close program by user')
            sys.exit()
        elif user_input == 'help':
            help_user()
            user_input = input('> ')

        num1, operator, num2 = parser(user_input)
        result = calculator(num1, operator, num2)

        if result.is_integer():
            print(f'> result: {int(result)}\n{40 * "-"}')
            logger(user_input, int(result))
        else:
            print(f'> result: {result}\n{40 * "-"}')
            logger(user_input, result)

    except ValueError:
        exception_logger(user_input, invalid_format)

    except ZeroDivisionError as e:
        exception_logger(user_input, e)

    except AssertionError as e:
        exception_logger(user_input, e)