from string import digits, ascii_letters, punctuation


class Account:
    __database = {}

    def __init__(self, username, password):
        self.__username = Account.valid_username(username)
        self.__password = Account.valid_password(password)
        Account.__database[self.__username] = self

    @property
    def username(self):
        return self.__username

    @property
    def password(self):
        return self.__password

    @staticmethod
    def valid_username(value):
        if value in Account.__database:
            raise Exception(f"username {value} already exist")
        if not 4 <= len(value) <= 8:
            raise Exception('username length must be 4 to 8 character')
        return value

    @staticmethod
    def valid_password(value):
        value = str(value)
        if not 8 <= len(value) <= 16:
            raise Exception('password length must be 8 to 16')

        digits_flag = letters_flag = punctuation_flag = False
        for ch in value:
            if ch in digits:
                digits_flag = True
            if ch in ascii_letters:
                letters_flag = True
            if ch in punctuation:
                punctuation_flag = True
        if digits_flag and letters_flag and punctuation_flag:
            return value

        # if any([True for i in value if i in digits]) and \
        #    any([True for i in value if i in ascii_letters]) and \
        #    any([True for i in value if i in punctuation]):
        #     return value
        raise Exception('password must contain digits, letters, punctuation')

    def change_password(self, old_password, new_password1, new_password2):
        if not old_password == self.__password:
            raise Exception('old password incorrect.')
        new_password1 = Account.valid_password(new_password1)
        new_password2 = Account.valid_password(new_password2)
        if not new_password1 == new_password2:
            raise Exception("new password doesn't match.")
        self.__password = new_password1




mojtaba = Account('mojtaba', '12345678h/')
print(mojtaba.username)
print(mojtaba.password)
mojtaba.change_password('12345678h/', '123456ab//', '123456ab//')
print(mojtaba.password)

