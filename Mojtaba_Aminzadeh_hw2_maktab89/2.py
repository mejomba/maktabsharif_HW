from functools import reduce
data = [2, 3, 5, 2]

# first way using lambda
out = reduce(lambda x, y: x*y, data)
print(out)

# second way using normal function
def mul(a, b):
    return a * b

out = reduce(mul, data)
print(out)

# third way without reduce
# def mul(data_list):
#     mul = 1
#     for num in data_list:
#         mul *= num
#     return mul

# print(mul(data))