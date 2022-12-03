class Base:
    variable = []

    def some_method(self):
        self.__class__.variable.append(self)
        # print(self.__class__.variable)
        # Base.variable.append(self)
        # Child.variable.append(self)
        print('base', Base.variable)
        print('child', Child.variable)


class Child(Base):
    # variable = []
    pass


base = Base()
child = Child()

base.some_method()
child.some_method()

