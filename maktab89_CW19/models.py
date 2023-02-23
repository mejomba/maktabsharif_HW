import psycopg2
from hashlib import sha256
import re
from database import UserContextManager, PostContextManager
from utils import get_digit, show_menu


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = User.__valid_password(password)

    @classmethod
    def create_user(cls, username, password):
        try:
            user = cls(username, password)
        except Exception as err:
            user = None
            return err

        if user:
            with UserContextManager() as U:
                U.insert_database(user)
            if U.err:
                return U.err
            if U.result:
                return U.result

    @staticmethod
    def login(username, password):
        hash_password = User.__valid_password(password)
        with UserContextManager() as U:
            U.login(username, hash_password)
        if U.err:
            return U.err, U.user
        if U.result:
            return U.result, U.user

    @staticmethod
    def __valid_password(password):
        password_regex = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$"
        if not re.match(password_regex, password):
            # todo: create custom exception for password validation
            raise Exception('password incorrect format')
        return sha256(str(password).encode()).hexdigest()


class Post:
    def __init__(self, title, body):
        self.title = title
        self.body = body

    @classmethod
    def create_post(cls, title, body, user_id):
        post = cls(title, body)
        if post:
            with PostContextManager() as P:
                P.insert_to_database(post, user_id=user_id)
            if P.err:
                return P.err
            if P.result:
                return P.result

    @staticmethod
    def my_post(user_id):
        with PostContextManager() as P:
            P.select_by_user_id(user_id=user_id)
        if P.err:
            return P.err, P.posts
        if P.result:
            return P.result, P.posts

    @staticmethod
    def all_post():
        with PostContextManager() as P:
            P.select_all_post()
        if P.err:
            return P.err, P.posts
        if P.result:
            return P.result, P.posts

menu = {
    '1': 'sign up',
    '2': 'sign in',
    '0': 'exit'
}
login_menu = {
    '1': 'create post',
    '2': 'my post',
    '3': 'all post',
    '0': 'logout'
}

while True:
    show_menu(menu)
    user_input = get_digit('> ')
    if user_input == 0:
        break
    if user_input == 1:
        """create account"""
        username = input('username: ')
        password = input('password: ')
        res = User.create_user(username, password)
        print(res)

    elif user_input == 2:
        username = input('username: ')
        password = input('password: ')
        result, user = User.login(username, password)
        print(result)
        if user:
            while True:
                show_menu(login_menu)
                user_input = get_digit('> ')
                if user_input == 1:
                    title = input('title: ')
                    body = input('body: ')
                    res = Post.create_post(title=title, body=body, user_id=user[0])
                    print(res)
                elif user_input == 2:
                    result, posts = Post.my_post(user_id=user[0])
                    if posts:
                        for post in posts:
                            print(post)
                elif user_input == 3:
                    result, posts = Post.all_post()
                    if posts:
                        for post in posts:
                            print(post)
                elif user_input == 0:
                    break
                else:
                    print('wrong input')
    else:
        print('wrong input')