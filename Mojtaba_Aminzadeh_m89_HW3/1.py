import time
from functools import lru_cache

def timer_process(func):
    def wraper(data):
        start = time.time()
        out = func(data)
        end = time.time()
        # print(f'process time for fibo({data}): {round(end - start, 6)} s')
        return f'process time for fibo({data}) : {round(end - start, 6)} s'
        # return out
    return wraper


@timer_process
# @lru_cache
def fibo(n):
    if n == 0:
        return 0
    if n in {1, 2}:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


x = fibo(30)
print(x)
# 1 1 2 3 5 8 13