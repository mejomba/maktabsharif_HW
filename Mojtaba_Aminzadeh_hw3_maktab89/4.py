import re


def write_to_file(data_set):
    with open('result.txt', 'w') as file:
        for item in data_set:
            print(item, file=file)


with open('iran.txt', 'r') as input_file:
    pattern = r'([A-Z]+[a-z]*)[\,\:\-\. \[\{\n]'
    string = input_file.read()
    result = re.findall(pattern, string)
    result = set(result)

    write_to_file(result)
