def do_before(func):
    def outer(f):
        def wraper():
            func()
            f()
        return wraper
    return outer


def func():
    print('this is called before')


@do_before(func)
def my_function():
    print('hello')

my_function()

