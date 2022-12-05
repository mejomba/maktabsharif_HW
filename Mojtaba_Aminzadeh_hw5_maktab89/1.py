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


a1 = A('mamad')
a2 = A('akbar', 30)

print(a1)
print(a2)
print(a1 is a2)
print(id(a1) == id(a2))
