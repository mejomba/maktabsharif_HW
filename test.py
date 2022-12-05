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
