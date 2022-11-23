invalid_number = 'Invalid Number Exception'
invalid_operator = 'Invalid Operator Exception'


def parser(user_input):
    num1, operator, num2 = user_input.split(' ')

    assert num1.isdigit() and num2.isdigit(), f'{invalid_number}'
    assert operator in {'+', '-', '*', '/'}, f'{invalid_operator}'
    return num1, operator, num2

