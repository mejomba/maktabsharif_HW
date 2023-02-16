from typing import Dict


def write_file(data: Dict):
    with open('phone.txt', 'a+') as file:
        for item in data.values():
            file.write(str(item) + " ")
        file.write('\n')


def read_file():
    with open('phone.txt', 'r') as file:
        while True:
            data = file.readline()
            if not data:
                break
            first_name, last_name, phone, email, _ = data.split(' ')
            yield first_name, last_name, phone, email