class Base():
    sum_ = 0

    def __call__(self, number):
        self.sum_ += number
        return self.sum_


class Add(Base):

    def __init__(self, number=0):
        self.number = self.__call__(number)

    def __call__(self, number):
        super().__call__(number)
        return self

    def __repr__(self):
        result = self.sum_
        self.sum_ = 0
        return str(result)


print(Add(50))  # --> 50
print(Add(50)(20)(10))  # --> 80

x = Add()
print(x(10)(20)(-30))  # --> 0
print(x(10)(20)(30))  # --> 60
print(x(10)(20)(30))  # --> 60
