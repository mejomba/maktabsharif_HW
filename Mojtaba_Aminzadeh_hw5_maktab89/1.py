class Singleton:
    __instance = None

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.__instance, cls):
            cls.__instance = super().__new__(cls)
        return cls.__instance


class A(Singleton):
    def __init__(self, name, age=20):
        self.name = name
        self.age = age


class B(Singleton):
    def __init__(self, name, age=None):
        self.name = name
        self.age = age


a1 = A('mamad')
a2 = A('akbar', 20)

print(a1)
print(a2)
print(a1 is a2)

b1 = B('jafar')
b2 = B('ahmad', 15)

print(b1)
print(b2)
print(b1 is b2)

