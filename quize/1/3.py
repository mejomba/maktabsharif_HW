class Number():
    def __init__(self, n):
        self.n = n
        self.type = self.check_type()
        print(self.type)

    def check_type(self):
        if isinstance(self.n, int):
            return int
        elif isinstance(self.n, float):
            return float

    def __add__(self, other):
        if self.check_type() == other.check_type():
            return self.n + other.n
        else:
            return "can not + between int and float"

    def __sub__(self, other):
        if self.check_type() == other.check_type():
            return self.n - other.n
        else:
            return "can not - between int and float"

    def __mul__(self, other):
        if self.check_type() == other.check_type():
            return self.n * other.n
        else:
            return "can not * between int and float"

    def __truediv__(self, other):
        if self.check_type() == other.check_type():
            return self.n / other.n
        else:
            return "can not / between int and float"

    def __eq__(self, other):
        return self.n == other.n

    def __ne__(self, other):
        return self.n != other.n

    def __gt__(self, other):
        return self.n > other.n

    def __ge__(self, other):
        return self.n >= other.n

    def __lt__(self, other):
        return self.n < other.n

    def __le__(self, other):
        return self.n <= other.n


print('\nbetween same type (int, int)...')
x = Number(4)
y = Number(5)

print('add', x + y)
print('sub', x - y)
print('mul', x * y)
print('dic', x / y)
print('eq', x == y)
print('not eq', x != y)
print('gt', x > y)
print('ge', x >= y)
print('lt', x < y)
print('le', x <= y)

print('\nbetween different type (float , int)...')
x = Number(12.5)
y = Number(8)

print('add', x + y)
print('sub', x - y)
print('mul', x * y)
print('dic', x / y)
print('eq', x == y)
print('not eq', x != y)
print('gt', x > y)
print('ge', x >= y)
print('lt', x < y)
print('le', x <= y)
