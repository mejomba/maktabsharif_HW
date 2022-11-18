def do_multi_times(num):
    def outer(f):
        def inner():
            for i in range(num):
                f()
        return inner
    return outer


@do_multi_times(3)
def salam():
    print('hello')


salam()