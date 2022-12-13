class Test:

    @classmethod
    def create(cls):
        if not hasattr(cls, 'jafar'):
            return cls.jafar
    pass


test = Test()
test.create()
print(Test.__dict__)
print(test.__dict__)