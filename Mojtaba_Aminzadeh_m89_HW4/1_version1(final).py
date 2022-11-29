from hashlib import sha256
import os
import sys
import time


try:
    import color
except ImportError:
    print('this program need "color" library')
    print('I try install this, if you got Error pleas install "color" library on your environment')
    time.sleep(3)
    if 'nt' in os.name:
        os.system('pip install color')
    else:
        os.system('pip3 install color')
    import color

red = color.red
blue = color.blue
green = color.green
yellow = color.yellow
# sha256(1234): 03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4
# sha256(123):  a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3


class User:
    id = 0
    user_registered = {}

    def __init__(self, username: str, password: str, phone_number: str = None):
        self.username = username
        self.__password = password
        if not phone_number:
            self.phone_number = 'not present'
        else:
            self.phone_number = phone_number
        User.id += 1
        self.id = User.id
        User.user_registered[self.id] = self
        print(f'{self.username} {green("registered")}\n')

    @staticmethod
    def __valid_pass(name_var, password):
        try:
            assert len(str(password)) >= 4, f"{name_var} length should be longer than 3"
            return sha256(str(password).encode('utf-8')).hexdigest()
        except AssertionError as e:
            print(f'{yellow("Hint:")} {e}')

    @staticmethod
    def __valid_username(username):
        try:
            for _user in User.user_registered.values():
                assert username != _user.username, f'{username} already taken'
            else:
                return username
        except AssertionError as e:
            print(f'{yellow("Hint:")} {e}')

    @classmethod
    def register_new_user(cls, username, password, phone):
        print(blue('========== register new user ==========\n'))
        if not username:
            print(yellow("hint: ") + "username can't be empty")
            print(red('Fail.'))
            return
        if not (user := cls.__valid_username(username)):
            print(red('Fail.'))
            return
        if not (passwd := cls.__valid_pass('password', password)):
            print(red('Fail.'))
            return
        phone = phone
        cls(user, passwd, phone)

    @staticmethod
    def login(_username, _password):
        print(blue('========== login ==========\n'))
        for _user in User.user_registered.values():
            if _username == _user.username and User.__valid_pass("password", _password) == _user.__password:
                # _user.id = _user_id
                return _user
        else:
            print(red('username or password incorrect.'))

    @staticmethod
    def change_password(_user, _old_password, _new_password1=None, _new_password2=None):
        print(blue('========== change_password ==========\n'))

        # check if password is valid, return sha256(password)
        _old_password = _user.__valid_pass("old_password", _old_password)
        if _old_password != _user.__password:
            print(f'> {red("your old password incorrect " )}')

            _new_password1 = _user.__valid_pass("new_password1", _new_password1)
            _new_password2 = _user.__valid_pass("new_password2", _new_password2)

            if _new_password1 != _new_password2 or not new_password1 or not _new_password2:
                input(f'''> {red("your new password don't match or empty. press Enter to menu ")}''')
            return

        if _new_password1 != _new_password2 or not new_password1 or not _new_password2:
            input(f'''> {red("your new password don't match or empty. press Enter to menu ")}''')
            return

        _new_password1 = _user.__valid_pass("new_password1", _new_password1)
        _new_password2 = _user.__valid_pass("new_password2", _new_password2)

        if _new_password1 and _new_password2:
            _user.__password = _new_password1

            # replace edited user with previous
            User.user_registered[_user.id] = _user
            print(green('password change success.'))
            return

    def user_information(self):
        print(blue('========== user information ==========\n'))
        print(self)

    def edit_username_and_phone(self, _username, _phone_number):
        print(blue('========== edit username and phone ==========\n'))
        # get new username and phone number
        try:
            for _user in User.user_registered.values():
                assert _username != _user.username, f'{_username} already taken.'
        except AssertionError as e:
            print(red(e))
            return

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


main_menu = {
    '1': 'register new user',
    '2': 'login',
    '0': 'exit'
}
_authenticated_menu = {
                '1': 'user information',
                '2': 'edit username and phone',
                '3': 'change password',
                '4': 'logout'
            }


def print_menu(menu):
    for item in menu:
        print(f'{item}: {menu[item]}')


if __name__ == "__main__":
    while True:
        # ==================== main menu ====================
        print(blue('========== main menu ==========\n'))
        print_menu(main_menu)

        user_input = input('\n> ')

        if user_input == '0':
            break

        op = main_menu.get(user_input)

        if op == 'register new user':
            username = input("> username: ")
            password = input("> password: ")
            phone = input("> phone: ")
            User.register_new_user(username, password, phone)
        elif op == 'login':
            username = input("> username: ")
            password = input("> password: ")
            if user := User.login(username, password):

                # ==================== authenticated menu ====================
                print(green('\nlogin success.'))
                print(green(f'welcome {username}\n'))
                while True:
                    print(blue('========== user authenticated menu ==========\n'))
                    print_menu(_authenticated_menu)

                    # ==================== get input for authenticated user operation ====================
                    _user_input = input('\n> ')
                    _op = _authenticated_menu.get(_user_input)

                    # ================= if valid operation make this name like python function name =================
                    if _op:
                        _op = _op.replace(' ', '_')

                    # ==================== handle input authenticated user operation ====================
                    # ==================== logout operation ====================
                    if _op == 'logout':
                        print('good by')
                        break

                    # ==================== change_password operation ====================
                    elif _op == 'change_password':
                        old_password = input("> old password [leave empty for exit]: ")
                        if not old_password:
                            continue
                        else:
                            new_password1 = input("> new password")
                            new_password2 = input("> repeat password")
                            User.change_password(user, old_password, new_password1, new_password2)

                    # ==================== edit_username_and_phone operation ====================
                    elif _op == 'edit_username_and_phone':
                        _username = input(f'> new username [leave empty for {user.username}]: ')
                        _phone_number = input(f'> new phone number: [leave empty for {user.phone_number}]\n'
                                              f'  or type {yellow("remove")} for remove your phone number: ')
                        user.edit_username_and_phone(_username, _phone_number)

                    # ==================== other operation ====================
                    elif _op:
                        exec(f'user.{_op}()')

                    # ==================== handle invalid input  ====================
                    else:
                        input(f'> {red("invalid input, press Enter to continue...")}')
        else:
            input(f'> {red("invalid input, press Enter to continue...")}')
