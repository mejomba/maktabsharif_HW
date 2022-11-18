import time





def process_timer(func):
    def inner_(arg):
        start = time.time()
        func(arg)
        end = time.time()
        print(f'process time for {arg} items is {end - start}s')
        return 'jafar'
    return inner_


@process_timer
def some(n):
    some_list = []
    for i in range(n):
        some_list.append(i)
    return some_list

print(some(1_000_000))

