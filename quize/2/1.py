from string import digits, ascii_letters, punctuation
from hashlib import sha256


class Account:
    database = {}
    id = 0

    def __init__(self, username, password):
        self._username = Account._valid_username(username)
        self.__password = Account._valid_password(password)
        Account.id += 1
        self.id = Account.id
        Account.database[Account.id] = self

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = Account._valid_password(password)

    @staticmethod
    def _valid_username(username):
        try:
            assert 4 <= len(username) <= 8, "username length 4 to 8 character"
            for user in Account.database.values():
                assert username != user.username, f'username {user.username} exist'
            return username
        except AssertionError as e:
            print(e)

    @staticmethod
    def _valid_password(password):
        try:
            password = str(password)
            assert 8 <= len(password) <= 16, 'password length 8 to 16'
            number_flag = False
            letter_flag = False
            symbol_flag = False
            for ch in password:
                if ch in digits:
                    number_flag = True
                if ch in ascii_letters:
                    letter_flag = True
                if ch in punctuation:
                    symbol_flag = True
            assert (number_flag and letter_flag and symbol_flag), 'password must contains, number, letters, special symbols'
            return sha256(password.encode('utf-8')).hexdigest()
        except AssertionError as e:
            print(e)

    def change_password(self, previous_pasword, new_password1, new_password2):
        try:
            assert self._valid_password(previous_pasword), 'your old password invalid'
            assert self._valid_password(new_password1), 'your new password 1 invalid'
            assert self._valid_password(new_password2), 'your new password 2 invalid'
            self.password = new_password1
            Account.database[self.id] = self
            # return new_password1
        except AssertionError as e:
            print(e)



mojtaba = Account('mojdsfsdftaba', '12345678a}')
jafar = Account('mojtaba', '12345678a}')
jafar2 = Account('mojtaba', '123456A,fd')
print(mojtaba.username)
print(jafar.username)
# jafar.username = 'dsaf'
print(jafar.username)

mojtaba.change_password("12345678a}", '1234abd}', '1234abc}')


