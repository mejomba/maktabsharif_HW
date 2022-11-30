from string import digits
from functools import reduce
from time import sleep

def unique_number(numbers):
    return reduce(lambda x, y: x + y, set(numbers))


def count_number(numbers):
    s = ''
    for d in digits:
        s += str(numbers.count(d))
    return reduce(lambda x, y: x + y ,filter(lambda x: x > '1', s))


def sort_number(numbers):
    return reduce(lambda x, y: x + y, sorted(numbers))


data = '442254545'
history = None
while data != history:
    print(data)
    history = data
    data = sort_number(count_number(data) + unique_number(data))
    sleep(0.3)
# output
# 442254545
# 223445
# 222345
# 23345
# 23452
# 22345