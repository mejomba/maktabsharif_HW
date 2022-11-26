from hashlib import sha256
import os
import sys
import time
import uuid
print(uuid.uuid5(uuid.NAMESPACE_DNS,"1"))
try:
    import color
except ImportError:
    print('this program need "color" library')
    print('I try install this, if you got Error pleas install "color" library in your environment')
    time.sleep(3)
    if 'nt' in os.name:
        os.system('pip install color')
    else:
        os.system('pip3 install color')

red = color.red
blue = color.blue
green = color.green
yellow = color.yellow
# sha256(1234): 03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4
# sha256(123):  a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3


class User:
    id = 1
    user_registered = {
    }

    def __init__(self, username: str, password: str, phone_number: str = None):
        self.username = username
        self.__password = password
        if not phone_number:
            self.phone_number = 'not present'
        else:
            self.phone_number = phone_number
        User.id += 1
        User.user_registered[User.id] = self
        print(f'{self.username} {green("registered")}\n')

    @staticmethod
    def __valid_pass(password):
        while True:
            try:
                assert len(str(password)) >= 4, f"password length should be longer than 3"
                return sha256(str(password).encode('utf-8')).hexdigest()
            except AssertionError as e:
                print(f'{red("Error:")} {e}')
                password = input('> password: ')

    @staticmethod
    def __valid_username(username):
        while True:
            try:
                for user_id, user in User.user_registered.items():
                    assert username != user.username, f'{username} already taken'
                else:
                    return username
            except AssertionError as e:
                print(f'{red("Error:")} {e}')
                username = input('> username: ')

    @classmethod
    def register_new_user(cls):
        print(blue('========== register new user ==========\n'))
        user = cls.__valid_username(input('> username: '))
        passwd = cls.__valid_pass(input('> password: '))
        phone = input('> phone number[optional]: ')
        cls(user, passwd, phone)

    @staticmethod
    def login():
        print(blue('========== login ==========\n'))
        _username = input('> username: ')
        _password = input('> password: ')
        for user_id, user in User.user_registered.items():
            if _username == user.username and User.__valid_pass(_password) == user.__password:
                return user.__authenticated()
        else:
            print(red('username or password incorrect.'))

    @staticmethod
    def change_password(user):
        print(blue('========== change_password ==========\n'))
        # get new password
        while True:
            _old_password = input(f'> old password [leave empty for exit]: ')
            if not _old_password:
                break

            # check if password is valid, save sha256(password)
            _old_password = user.__valid_pass(_old_password)
            if _old_password != user.__password:
                input(f'> {red("your old password incorrect. press Enter for try again" )}')
                continue

            _new_password_1 = input(f'> new password: ')
            _new_password_1 = user.__valid_pass(_new_password_1)

            _new_password_2 = input(f'> repeat new password: ')
            _new_password_2 = user.__valid_pass(_new_password_2)

            if _new_password_1 != _new_password_2:
                input(f'''> {red("your new password don't match. press Enter for try again")}''')
                continue

            user.__password = _new_password_1

            # replace edited user with previous
            User.user_registered[user.id] = user
            print(green('password change success.'))
            break

    @staticmethod
    def exit():
        print('tamam')
        sys.exit()

    def __authenticated(self):
        print(green('\nlogin success.'))
        print(green(f'welcome {self.username}\n'))
        while True:
            print(blue('========== user authenticated menu ==========\n'))
            _authenticated_menu = {
                '1': 'user information',
                '2': 'edit username and phone',
                '3': 'change password',
                '4': 'logout'
            }
            for _item in _authenticated_menu:
                print(f'{_item}: {_authenticated_menu[_item]}')
            _user_input = input('\n> ')
            _op = _authenticated_menu.get(_user_input).replace(' ', '_')
            if _op == 'logout':
                print('good by')
                input('> pres Enter to menu')
                break
            if _op == 'change_password':
                self.change_password(self)
            elif _op:
                exec(f'self.{_op}()')

    def user_information(self):
        print(blue('========== user information ==========\n'))
        print(self)

    def edit_username_and_phone(self):
        print(blue('========== endit username and phone ==========\n'))
        # get new username and phone number
        while True:
            _username = input(f'> new username [leave empty for {self.username}]: ')
            try:
                for _user_id, _user in User.user_registered.items():
                    assert _username != _user.username, f'{_username} already taken.'
                else:
                    break
            except AssertionError as e:
                print(red(e))
        _phone_number = input(f'> new phone number: [leave empty for {self.phone_number}]\n'
                              f'  or type {yellow("remove")} for remove your phone number: ')

        # set new value to user object
        if _username:
            self.username = _username

        if _phone_number == 'remove':
            self.phone_number = 'not present'
        elif _phone_number:
            self.phone_number = _phone_number

        # replace edited user with previous
        User.user_registered[self.id] = self

        # print success message
        print(green('\nusername and phone number edit successful.\n'))

    def __str__(self):
        return f'username: {self.username}\nphone: {self.phone_number}\n'

    def __repr__(self):
        return f'username: {self.username}\nphone: {self.phone_number}\npassword: hashed'


menu = {
    '1': 'register new user',
    '2': 'login',
    '0': 'exit'
}

while True:
    print(blue('========== main menu ==========\n'))
    for item in menu:
        print(f'{item}: {menu[item]}')
    user_input = input('\n> ')
    if user_input == '0':
        break
    op = menu.get(user_input)
    if op:
        op = op.replace(' ', '_')
        eval(f'{User.__name__}.{op}()')
    else:
        input(f'> {red("invalid input, press Enter to continue...")}')
