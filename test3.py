class Add:

    def __init__(self, number=0):
        self.number = number

    def __call__(self, *args, **kwargs):
        self.number += args[0]
        return self

    def __repr__(self):
        return str(self.number)


# x = Add()
# print(x(10)(20)(10)(5)(-2))
#
# print(Add(10)(20)(5)(3))

#
# class Add:
#
#     def __init__(self, number=0):
#         self.number = number
#
#     def __call__(self, num):
#         self.number += num
#         return self
#
#     def __repr__(self):
#         return str(self.number)
#
#
# x = Add()
# print(x(10)(20)(10)(5)(-2))
#
# print(Add(10)(20)(5)(3))

class add(int):
    def __call__(self, value):
        return add(self + value)


print(add(5)(10)(20)(4))

from test import *
import test
from test import _a
print(_a
)