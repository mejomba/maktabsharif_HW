class Add:

    def __init__(self, number=0):
        self.number = number

    def __call__(self, *args, **kwargs):
        self.number = self.add(args[0])
        return self

    def add(self, value):
        self.number += value
        return self.number

    def __repr__(self):
        return str(self.number)


x = Add()
print(x(10)(20)(10)(5)(-2))

print(Add(10)(20)(5)(3))
# ======================
# ======================

# class A:
#     def __init__(self, name, age):
#         self._name = name
#         self.__age = age
#
#     def __get_age(self):
#         print(self.__age)
#
# class B(A):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def get_name(self):
#         print(self._name)
#
#     def get_age(self):
#         A._A__get_age(self)
#
# b = B('jafar', 20)
# b.get_age()
# b.get_name()

# ==============================
# ==============================
import os
# os.popen()

class OsUtils:

    @staticmethod
    def generate_file(file_name):
        os.system(f'touch {file_name}')
        # os.popen(f'touch {file_name}')

    @staticmethod
    def generate_directory(path, directory_name):
        if path:
            path = path.strip('/')
            os.system(f'mkdir {path}/{directory_name}')
        else:
            os.system(f'mkdir {directory_name}')

    @staticmethod
    def file_directory_list(directory_name):
        os.system(f'ls {directory_name}')

    def edit_name(self):
        pass

    def move_file(self):
        pass

    @staticmethod
    def copy_file(source, destination):
        os.system(f'cp {source} {destination}')

    @staticmethod
    def delete_file(file_name):
        os.system(f'rm {file_name}')

    @staticmethod
    def delete_directory(directory_name):
        pass

# OsUtils.generate_file('salam.py')
# OsUtils.delete_file('salam.py')
# OsUtils.copy_file('test2.py', 'quize/')
# OsUtils.generate_directory('', 'jafar')
# OsUtils.file_directory_list('./ostad_code')







class A:
    pure_number = 0

    def __call__(self, a):
        self.pure_number += a
        return A()

    def __repr__(self):
        return f"{self.pure_number}"


Add = A()
Add2 = A()
print(Add(2)(10)(10)(16)(18))
print(Add2(2)(10)(10)(16)(18))

def __a():
    print('salam')
_a = 500