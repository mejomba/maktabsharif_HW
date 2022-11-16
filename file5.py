def read_file(file_name):
    with open(file_name, 'r') as file_handler:
        while True:
            data = file_handler.readline()
            if not data:
                break
            yield data


input_file_name = input('input_file_name: ')

generator_file_object = read_file(input_file_name)

for line in generator_file_object:
    print(line, end='')


