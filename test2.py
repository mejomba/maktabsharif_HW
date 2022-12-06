class a:
    def func(self):
        print("Hello, you are now in class A")


class b(a):
    def func(self):
        super().func()
        print("Hello, you are now in class B")


class c(a):
    def func(self):
        super().func()
        print("Hello, you are now in class C")


class d(b, c):
    def func(self):
        super().func()


ref = d()
ref.func()
# ============================
# ============================
