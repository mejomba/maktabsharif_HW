from os import name as os_name, system as terminal
import sys


def clear():
    terminal('cls' if os_name.lower() == 'nt' else 'clear')


def register_phone_number():
    clear()
    print("------ Register ------")
    phone_number = input("Enter phone number [valid phone number = 09123334444] : ")

    # len = 11
    # phone_number[:2] = '09'

    assert len(phone_number) == 11 and phone_number[:2] == '09', "phone number is not valid !"

    fullname = input("Enter phone name : ")

    # str , numeric

    assert not fullname.isnumeric(), "fullname not valid !"

    with open("phonebooks.txt", "a+") as db:
        db.write(f"{fullname}::{phone_number}\n")

    input("Your number saved ! \n\nPress enter to back main ... ")


def read_file(name):
    with open(name, 'r') as file:
        while True:
            data = file.readline()
            if not data:
                break
            else:
                yield data


def list_phone_numbers():
    file_generator = read_file('phonebooks.txt')

    for line in file_generator:
        print(line, end='')

    print('-' * 24)
    input('Enter To Menu... ')


def search_phone_numbers():
    query = input('your query for search: ')
    assert len(query) >= 3, 'query len must be greater than 2 '

    file_generator = read_file('phonebooks.txt')
    result = list(filter(lambda x: query in x, file_generator))

    print(f'result for "{query}" is\n', *result)
    input('Enter To Menu... ')


def about():
    print('about this program...\n')
    input('Enter To Menu... ')


def exit():
    sys.exit()


menu_items = [
    'register phone number',
    'list phone numbers',
    'search phone numbers',
    'about',
    'exit',
]

line = "-" * 22
user_number = None
while user_number != 5:
    clear()
    print("-------- Menu --------")

    for index, value in enumerate(menu_items):
        print(index + 1, value)
    print(line)

    try:
        user_number = int(input("> "))
        func = menu_items[user_number - 1]
        func = func.replace(" ", "_")

        eval(f"{func}()")

    except (ValueError, IndexError):
        input("Error !!! \n\nPress enter to back main ... ")

    except AssertionError as msg:
        input(msg)
        eval(f"{func}()")
