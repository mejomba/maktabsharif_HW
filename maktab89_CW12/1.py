import re


class FilteredEditor:
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode

    def __enter__(self):
        try:
            self.file = open(self.path, mode=self.mode)
            return self.file
        except FileNotFoundError as e:
            print(e.strerror)
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(exc_type)
        # print(exc_val)
        # print(exc_tb)
        if file:
            self.file.close()
        return True


path = 'bad_word.txt'
user_input = 'salam man biadab hastam to khobi mostafa'
words = {}
with FilteredEditor(path, 'r') as file:
    if file:
        for item in file:
            new_item = item.split(',')
            words[new_item[0]] = new_item[1].strip('\n')

        for item in words:
            if item in user_input:
                user_input = re.sub(item, words.get(item), user_input)
        print(user_input)
