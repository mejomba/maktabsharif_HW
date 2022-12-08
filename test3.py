class Add:

    def __init__(self, number=0):
        self.number = number

    def __call__(self, *args, **kwargs):
        self.number += args[0]
        return self

    def __repr__(self):
        return str(self.number)


x = Add()
print(x(10)(20)(10)(5)(-2))

print(Add(10)(20)(5)(3))

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

RED = "\033[0;31m"
GREEN = "\033[0;32m"
BLUE = "\033[0;34m"
YELLOW = "\033[1;33m"
END = "\033[0m"

print(f'{RED}salam')
print(f'{END}salam')