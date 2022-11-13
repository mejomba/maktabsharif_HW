from functools import wraps

def deco_outer(a, b):
    def outer(func):
        @wraps(func)
        def inner(n):
            print(a, b)
            t = func(n)
            return t.upper()
        return inner
    return outer


def split(func):
    @wraps(func)
    def inner_split(n):
        return func(n).split()
    return inner_split

@split
@deco_outer('mamad', "nobari")
def show(name):
    return f'salam {name}'

print(show('jafar'))
print(show.__name__)

