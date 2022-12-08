from hashlib import sha256
from typing import Optional


RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
YELLOW = "\033[1;33m"
END = "\033[0m"

# sha256(1234): 03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4
# sha256(123):  a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3


class User:
    id = 0
    user_registered = {}
    """User class for generate user and register in database
    :param id: like database primary key
    :param user_registered: a dictionary use as database
    """

    def __init__(self, username: str, password: str, phone_number: Optional[str] = None):
        """
        :param username:str, required, non duplicate
        :param password:str, minimum length 4 character
        :param phone_number: str, optional
        """
        self.username = username
        self.__password = password
        if not phone_number:
            self.phone_number = 'not present'
        else:
            self.phone_number = phone_number
        User.id += 1
        self.id = User.id
        User.user_registered[self.id] = self
        print(f'{self.username} {GREEN}"registered"\n{END}')

    @staticmethod
    def __valid_pass(name_var: str, password: str) -> str:
        """
        check password validation and return sha256(password)
        :param name_var: variable name show in message
        :param password: user input password
        :return: str
        """
        try:
            assert len(str(password)) >= 4, f"{name_var} length should be longer than 3"
            return sha256(str(password).encode('utf-8')).hexdigest()
        except AssertionError as e:
            print(f'{YELLOW}("Hint:"){END}', e)

    @staticmethod
    def __valid_username(username: str) -> str:
        """
        check for non duplicated username
        :param username: str from user input
        :return: str
        """
        try:
            for _user in User.user_registered.values():
                assert username != _user.username, f'{username} already taken'
            else:
                return username
        except AssertionError as e:
            print(f'{YELLOW}("Hint:"){END}', e)

    @classmethod
    def register_new_user(cls, username: str, password: str, phone: str) -> None:
        """
        if username and password is valid call User class for initiate new User instance
        :param username: str form user input
        :param password: str from user input
        :param phone: str optional from user input
        :return: None
        """
        print(f'{BLUE}========== register new user ==========\n{END}')
        if not username:
            print(f"{YELLOW}hint: " + "username can't be empty{END}")
            print(f'{RED}Fail.{END}')
            return
        if not (user := cls.__valid_username(username)):
            print(f'{RED}Fail.{END}')
            return
        if not (passwd := cls.__valid_pass('password', password)):
            print(f'{RED}Fail.{END}')
            return
        phone = phone
        cls(user, passwd, phone)

    @staticmethod
    def login(_username: str, _password: str) -> None:
        """
        if _username and _password in database user authenticated
        :param _username: str from user input
        :param _password: str from user input
        :return: user
        """
        print(f'{BLUE}========== login ==========\n{END}')
        for _user in User.user_registered.values():
            if _username == _user.username and User.__valid_pass("password", _password) == _user.__password:
                # _user.id = _user_id
                return _user
        else:
            print(f'{RED}username or password incorrect.{END}')

    @staticmethod
    def change_password(_user: 'User', _old_password: str, _new_password1=None, _new_password2=None) -> None:
        """
        change password if user old password and new password1 and 2 is valid
        :param _user: user object who want to change password
        :param _old_password: str from user input
        :param _new_password1: str from user input
        :param _new_password2: str from user input
        :return: None
        """
        print(f'{BLUE}========== change_password ==========\n{END}')

        # check if password is valid, return sha256(password)
        _old_password = _user.__valid_pass("old_password", _old_password)
        if _old_password != _user.__password:
            print(f'> {RED}"your old password incorrect "{END} ')

            _new_password1 = _user.__valid_pass("new_password1", _new_password1)
            _new_password2 = _user.__valid_pass("new_password2", _new_password2)

            if _new_password1 != _new_password2 or not new_password1 or not _new_password2:
                input(f'''> {RED}"your new password don't match or empty. press Enter to menu"{END} ''')
            return

        if _new_password1 != _new_password2 or not new_password1 or not _new_password2:
            input(f'''> {RED}"your new password don't match or empty. press Enter to menu"{END} ''')
            return

        _new_password1 = _user.__valid_pass("new_password1", _new_password1)
        _new_password2 = _user.__valid_pass("new_password2", _new_password2)

        if _new_password1 and _new_password2:
            _user.__password = _new_password1

            # replace edited user with previous
            User.user_registered[_user.id] = _user
            print(f'{GREEN}password change success.{END}')
            return

    def user_information(self):
        print(f'{BLUE}========== user information ==========\n{END}')
        print(self)

    def edit_username_and_phone(self, _username, _phone_number):
        """
        this method edit username and phone number
        :param _username: str from user input
        :param _phone_number: str from user input
        :return: None
        """
        print(f'{BLUE}========== edit username and phone ==========\n{END}')
        # get new username and phone number
        try:
            for _user in User.user_registered.values():
                assert _username != _user.username, f'{_username} already taken.'
        except AssertionError as e:
            print(f'{RED}{e}{END}')
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
        print(f'\n{GREEN}username and phone number edit successful.\n')

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
        print(f'{BLUE}========== main menu ==========\n{END}')
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
                print(f'\n{GREEN}login success.{END}')
                print(f'{GREEN}welcome {username}\n{END}')
                while True:
                    print(f'{BLUE}========== user authenticated menu ==========\n{END}')
                    print_menu(_authenticated_menu)

                    # ==================== handle input authenticated user operation ====================
                    _user_input = input('\n> ')
                    _op = _authenticated_menu.get(_user_input)
                    if _op:
                        _op = _op.replace(' ', '_')

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
                                              f'  or type {YELLOW}"remove"{END} ' + 'for remove your phone number: ')
                        user.edit_username_and_phone(_username, _phone_number)

                    # ==================== other operation ====================
                    elif _op:
                        exec(f'user.{_op}()')

                    # ==================== handle invalid input  ====================
                    else:
                        input(f'> {RED}"invalid input, press Enter to continue..." {END}')
        else:
            input(f'> {RED}"invalid input, press Enter to continue..." {END}')
