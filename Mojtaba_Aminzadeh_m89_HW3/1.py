import time
from functools import lru_cache

def write_file(data, result):
    with open('cache.txt', 'a+') as file:
        file.seek(0)
        prev_data = file.read()
        new_data = str(data) + " " + str(result)
        if not new_data in prev_data:
            print(new_data, file=file, flush=True)


def read_file(name):
    with open(name, 'r') as file:
        while True:
            data = file.readline()
            if not data:
                break
            k, v = data.split()
            yield k, v


def cache_dict():
    d = {}
    cache_data = read_file('cache.txt')
    for item in cache_data:
        d[int(item[0])] = int(item[1])
    return d


# cache_dict = cache_dict()


# def cache(func):
#     '''calculate new fibo() in not in cache.txt write in file'''
#     result = None
#     def wrapper(data):
#         nonlocal result
#         if not data in cache_dict.keys():
#             result = func(data)
#             write_file(data, result)
#             return result
#         else:
#             return cache_dict[data]
#     return wrapper


# def cache(func):
#     result = {}
#     def wrapper(data):
#         nonlocal result
#         if not data in result:
#             result[data] = func(data)
#             # write_file(data, result)
#             return result[data]
#         else:
#             return data
#     return wrapper


def cache(func):
    result = cache_dict()
    def wrapper(data):
        nonlocal result
        if not data in result.keys():
            result[data] = func(data)
            write_file(data, result[data])
        return result[data]
    return wrapper


def timer_process(func):
    def wraper(data):
        start = time.time()
        out = func(data)
        end = time.time()
        print(f'process time for fibo({data}) : {round(end - start, 6)} s')
        return out
    return wraper


@timer_process
@cache
def fibo(n):
    if n == 0:
        return 0
    if n in {1, 2}:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


# @timer_process
# # @cache
# def factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n * factorial(n-1)


x = fibo(155)
print(x)
