import contextlib
import time


@contextlib.contextmanager
def Timer(user_input):
    if user_input == 'second':
        start = time.time()
        yield
        end = time.time()
        print(f'time: {end - start}')
    elif user_input == 'ns':
        start = time.time_ns()
        yield
        end = time.time_ns()
        print(f'time_ns: {end - start}')


user_input = input('Enter "second" of "ns": ')
with Timer(user_input):
    li = []
    for i in range(1000):
        for j in range(1000):
            li.append((i, j))


with Timer(user_input):
    x = [(i, j) for i in range(1000) for j in range(1000)]
