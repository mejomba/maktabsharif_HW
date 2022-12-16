from abc import ABC, abstractmethod


class Abstract(ABC):

    @abstractmethod
    def method(self):
        pass


class Parent(Abstract):
    def method(self):
        pass
    pass


class Child(Parent):
    pass

p = Parent()
c = Child()