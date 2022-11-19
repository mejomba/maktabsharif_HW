import re
pattern = re.compile('(^[A-Z]+[A-Za-z]*)\s')

# pattern = r'(^[A-Z]+[A-Za-z]*) '
def write_to_file(data):
    with open('result.txt', 'a') as file:
        print(data, file=file)


with open('iran.txt', 'r') as input_file:
    string = input_file.read()
    result = re.findall(pattern, string)
    print(result)
    # if 1 == 1:
    #     write_to_file(result)