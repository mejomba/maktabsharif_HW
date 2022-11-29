from pprint import pprint


class Student:
    def __init__(self, first_name, last_name, age, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.phone = phone
        self.email = email

    def data(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'email': self.email
            }

reza = Student('Reza', 'Amiri', 22, 9123334444, 'mail@gmail.com')
pprint(reza.data())
pprint(type(reza.data()))

