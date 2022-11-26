import time
from functools import lru_cache
import sys, os


def write_file(chach_file, data, result):
    with open(chach_file, 'a+') as file:
        kb = 1000
        file.seek(0)
        prev_data = file.read()
        if not sys.getsizeof(prev_data) / kb > 499:
            new_data = str(data) + " " + str(result)
            if not new_data in prev_data:
                print(new_data, file=file, flush=True)


def read_file(cache_file):
    with open(cache_file, 'r') as file:
        while True:
            data = file.readline()
            if not data:
                break
            k, v = data.split()
            yield k, v


def cache_dict(cache_file):
    d = {}
    cache_data = read_file(cache_file)
    for item in cache_data:
        d[int(item[0])] = int(item[1])
    return d


def cache(cache_file):
    def inner_cache(func):

        result = cache_dict(cache_file)
        def wrapper(data):
            nonlocal result
            if not data in result.keys():
                result[data] = func(data)
                write_file(cache_file, data, result[data])
            return result[data]

        return wrapper
    return inner_cache


def timer_process(func_name: str):
    def inner_timer_process(func):
        def wraper(data):

            start = time.time()
            val = func(data)
            end = time.time()
            print(f'process time for {func_name} ({data}) : {round(end - start, 6)} s')
            # print(start, end)
            # return f'process time for {func_name} ({data}) : {round(end - start, 10)} s'
            return val

        return wraper
    return inner_timer_process


@timer_process('fibo')
@cache('fibo_cache.txt')
def fibo(n):
    if n in {1, 2}:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


@timer_process('factorial')
@cache('factorial_cache.txt')
def factorial(n):
   if n == 1:
       return n
   else:
       return n * factorial(n-1)


fibonacci = fibo(20)
# fact = factorial(5)

print('fibonacci: ', fibonacci)
# print('fact: ', fact)

# fibo 200 without "fibo_cache.txt" = 0.028
# fibo 200 wit "fibo_cache.txt" = 0.000002
# fibo 400 wit fibo(200) cache = 0.013
# 0.002