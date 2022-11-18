from functools import reduce
# 1 1 2 3 5
def fib(n):
    a, b = 1, 1
    while a < n:
        yield a
        x = a + b
        a = b
        b = x

x = fib(10)

print(type(x))


s = reduce(lambda x, y: x + y, filter(lambda x: x % 2 ,x))
print(s)
