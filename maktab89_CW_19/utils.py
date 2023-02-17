from typing import Dict





def show_menu(m: Dict):
    for k, v in m.items():
        print(f'{k}: {v}')


def get_digit(prompt):
    user_input = input(prompt)
    if user_input.isdigit():
        return int(user_input)
    return ''
