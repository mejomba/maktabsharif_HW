from hashlib import sha256
import os


# sha256(1234): 03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4
# sha256(123):  a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3

def clear():
    os.system('cls') if 'nt' in os.name else os.system('clear')


class User:
    id = 0
    user_registered = {
    }

    def __init__(self, username: str, password: str, phone_number: str = None):
        self.username = username
        self.__password = self.__valid_pass(password)
        self.phone_number = phone_number
        User.id += 1

    @staticmethod
    def __valid_pass(password):
        assert len(str(password)) >= 4, "password length should be longer than 3"
        return sha256(str(password).encode('utf-8')).hexdigest()

    def get_pass(self):
        print(self.__password)

    @classmethod
    def register_new_user(cls):
        pass

    @staticmethod
    def login(_username, _password):
        for user_id, user in User.user_registered.items():
            if _username == user.username and User.__valid_pass(_password) == user.__password:
                print('login success.')
                print(f'{user_id}: {user}')
            else:
                print('username or password incorrect.')

    def cahnge_password(cls):
        print('change_password method\n')

    def logout(cls):
        print('logout method\n')


menu = {
    '1': 'register new user',
    '2': 'login',
    '3': 'change password',
    '4': 'logout'
}

while True:
    # clear()
    for item in menu:
        print(f'{item}: {menu[item]}')
    user_input = input('\n> ')
    if user_input == '0':
        break
    op = menu.get(user_input)
    if op == 'login':
        input_username = input('> username: ')
        input_password = input('> password: ')
        User.login(input_username, input_password)
    # if op:
    #     op = op.replace(' ', '_')
    #     print(op)
    #     eval(f'{User.__name__}.{op}()')
    # else:
    #     input('> invalid input, press Enter to continue...')

mojtaba = User('mejomba', '1234')
mojtaba.get_pass()