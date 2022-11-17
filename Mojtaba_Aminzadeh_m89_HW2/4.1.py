from string import digits
from functools import reduce
from time import sleep

def unique_number(numbers):
    try:
        return reduce(lambda x, y: x + y, set(numbers))
    except:
        return ''


def count_number(numbers):
    s = ''
    for d in digits:
        s += str(numbers.count(d))
    try:
        return reduce(lambda x, y: x + y ,filter(lambda x: x > '1', s))
    except TypeError:
        return ''


def sort_number(numbers):
    try:
        return reduce(lambda x, y: x + y, sorted(numbers))
    except TypeError:
        return ''


data = '442254545'
history = None
while data != history:
    print(data)
    history = data
    data = sort_number(count_number(data) + unique_number(data))
    sleep(0.5)
# output
# 442254545
# 223445
# 222345
# 23345
# 23452
# 22345