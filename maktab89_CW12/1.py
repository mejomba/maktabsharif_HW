import re


class FilteredEditor:
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode
        self.words = {}

    def __enter__(self):
        try:
            self.file = open(self.path, mode=self.mode)
            return self
        except FileNotFoundError as e:
            print(e.strerror)
            return None

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(exc_type)
        # print(exc_val)
        # print(exc_tb)
        if file:
            self.file.close()
        # return True

    def filter_word(self, user_input):
        if self.file:
            for item in self.file:
                new_item = item.split(',')
                self.words[new_item[0]] = new_item[1].strip('\n')

            for item in self.words:
                if item in user_input:
                    user_input = re.sub(item, self.words.get(item), user_input)
            return user_input


path = 'bad_word.txt'
user_input = 'salam man biadab hastam to khobi mostafa'
with FilteredEditor(path, 'r') as file:
    result = file.filter_word(user_input)
    print(result)