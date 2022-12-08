class A:
    def func(self):
        print("Hello, you are now in class A")


class B(A):
    def func(self):
        super().func()
        print("Hello, you are now in class B")


class C(A):
    def func(self):
        super().func()
        print("Hello, you are now in class C")


class X(A):
    def func(self):
        super().func()
        print("Hello, you are now in class C")


class D(B, C, X):
    def func(self):
        super().func()


obj = D()
obj.func()
