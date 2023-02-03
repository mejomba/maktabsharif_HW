import argparse
import pickle
from datetime import datetime
import shutil


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_info(self):
        return self.name

    def append_file(self):
        with open('user.pkl', 'ab') as file:
            pickle.dump(self, file)


class SuperUser(User):
    def __init__(self, name, email):
        super().__init__(name, email)
        self.is_superuser = True


def read_user():
    with open('user2 2023-02-03.backup', 'rb') as file:
        user_list = []
        try:
            while True:
                user_list.append(pickle.load(file))
        except EOFError:
            return user_list


def get_backup(file_name):
    today = datetime.now().strftime(' %Y-%m-%d')
    file_name += today + '.backup'
    shutil.copy('user.pkl', file_name)


parser = argparse.ArgumentParser()
parser.add_argument('--createuser', help="create new user and store")
parser.add_argument('--createsuperuser', help="create super user and store")
parser.add_argument('--showList', action='store_true', help="show all user list")
parser.add_argument('--Backup', help="backup all user with datetime")
parser.add_argument('--Restore', help="restore user from file")

args = parser.parse_args()
print(args)
if args.createuser:
    user_email = input("> user email: ")
    user = User(args.createuser, user_email)
    user.append_file()
    print(user.name, user.email)

elif args.createsuperuser:
    user_email = input("> super user email: ")
    super_user = SuperUser(args.createsuperuser, user_email)
    super_user.append_file()

elif args.showList:
    all_user = read_user()
    for user in all_user:
        if isinstance(user, SuperUser):
            print(f'{user.name} : {user.email} is super user')
        else:
            print(f'{user.name} : {user.email}')

elif args.Backup:
    get_backup(file_name=args.Backup)

elif args.Restore:
    print('restore')
    shutil


