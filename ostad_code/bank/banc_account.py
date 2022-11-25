import re


class Bank:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Saderat(Bank):
    def __init__(self, name, id, customers):
        self.customers = customers
        super().__init__(name, id)

    def save_customer(self, name, last_name, phone, deposit):
        pattern = r'([a-zA-Z]+.*)='
        with open(self.customers, 'a+') as customers_file:
            customers_file.seek(0)
            all_customer = re.findall(pattern, customers_file.read())
            if f'{name} {last_name}' in all_customer:
                print(f'"{name} {last_name}" currently exist in bank "{self.name}"')
            else:
                print(f'{name} {last_name}= phone: {phone} deposit: {deposit}', file=customers_file)


    def deposit(self):
        pass


class Sepah(Bank):
    def __init__(self, name, id, customers):
        self.customers = customers
        super().__init__(name, id)

    def save_customer(self, name, last_name, phone, deposit):
        pattern = r'([a-zA-Z]+.*)='
        with open(self.customers, 'a+') as customers_file:
            customers_file.seek(0)
            all_customer = re.findall(pattern, customers_file.read())
            if f'{name} {last_name}' in all_customer:
                print(f'"{name} {last_name}" currently exist in bank "{self.name}"')
            else:
                print(f'{name} {last_name}= phone: {phone} deposit: {deposit}', file=customers_file)

    def deposit(self):
        pass



class Account:
    def __init__(self, profile, username: str, user_last_name: str, phone: str, first_deposit: int):
        self.profile = profile
        self.username = username
        self.user_last_name = user_last_name
        self.phone = phone
        self.first_deposit = first_deposit

        self.save_profile()


    def save_profile(self):
        self.profile.save_customer(self.username, self.user_last_name, self.phone, self.first_deposit)

    def __add__(self, other):
        print(self.first_deposit + other.first_deposit)

    def get_balance(self):
        print(f'{self.profile}')


    def deposit(self, amount):
        pass

saderat = Saderat('bank_saderat', 123, 'saderat_customers.txt')
sepah = Sepah('bank_sepah', 456, 'sepah_customers.txt')

ali_acc = Account(saderat, 'ali', 'amini', '09112223344', 2000)
jafar_acc = Account(saderat, 'jafar', 'amini', '09112223344', 2000)
jafar_acc = Account(sepah, 'jafar', 'amini', '09112223344', 2000)

# jafar_acc + ali_acc

"""
Bank
-> Saderat
-> Sepah
Account:
--> save in file | validation
--> profile -> composite پروفایل یک کامپوزیت توی اکانت
--> validation روی ورودی ها یکم گیر بده به شماره تلفن و فرمت ها
--> + - len
reza_acc = Account واریز و برداشت داشته باشه با محدودیت مقدار 
# Account.register() || @classmethod

telegram@mrrezayazdani
rocket@r.yazdani
"""