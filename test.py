# ages = []
# for _ in range(3):
#     ages.append(int(input()))
#
# ages.sort()
# print("min", ages[0])
# print("max", ages[-1])
#
# print("max: ", max(ages))
# print('min: ',min(ages))
#
#
#
#
# 'a'.replace()
# grade = int(input("grade: "))
# if grade < 25:
#     print("F")
# elif 25 <= grade < 45:
#     print("E")
# elif 45 <= grade < 50:
#     print("D")
# elif 50 <= grade < 60:
#     print("E")
# elif 60 <= grade < 80:
#     print("B")
# elif grade > 80:
#     print("A")
#
#
#
# temp = input().upper()
# c = int(temp[:-1])
# f = int(temp[:-1])
# #
# if 'C' in temp:
#     f = c * (9 / 5) + 32
#     print(f'{int(f)}F')
# else:
#     c = (f-32) * (5/9)
#     print(f"{int(c)}C")
#
# # number = int(input())
# # for i in range(1, 11):
# #     print(i * number)
# #
# # print([number*i for i in range(1, 11)])
# #
# income = int(input("income: "))
# tax = 0
# if income < 10000:
#     print(tax)
# elif income < 20000:
#     tax = (income - 10000) * 0.1
#     print(tax)
# else:
#     tax = ((income - 20000) * 0.2) + 1000
#     print(tax)
#
#


# inp = input().split(',')
# sym = ['@', '#', '!']
# for email in inp:
#     upper_flag = False
#     lower_flag = False
#     digit_flag = False
#     symbol_flag = False
#     if 6 < len(email) < 12:
#         for ch in email:
#             if ch.isupper():
#                 upper_flag = True
#             if ch.islower():
#                 lower_flag = True
#             if ch.isdigit():
#                 digit_flag = True
#             if ch in sym:
#                 symbol_flag = True
#
#         if upper_flag and lower_flag and digit_flag and symbol_flag:
#             print(email)

# import re
# inp = input().split(',')
# pattern = r'(?=.*[A-Za-z])(?=.*\d)(?=.*[@$#&])[A-Za-z\d@$#&]{6,12}$'
# for password in inp:
#
#     result = re.findall(pattern, password)
#     print(*result)

# print(sum('12'))
from hashlib import sha256
from _md5 import md5
# from _sha256 import sha256
# x = sha256('fsdfdsfsdfdsfsdf'.encode('utf-8')).hexdigest()
# print(x)
# 1d7ae6ca9e689a549f4f47ba797e73dd9506182111a8e4157ad0945ca6ee419f
# 09b6f1b098ba521ff3492b1105974cc888d75d37d8457814123bf8cfc11e572f
# n = int(input())
# x = lambda n: not [i for i in range(2, n) if not (n%i)]
# y = lambda N: [i for i in range(2, N+1) if x(i)]
# print(y(n))

# def is_primal(n):
#     n = int(n)
#     assert n > 0
#     for i in range(2, int(n**0.5)+1):
#         if not (n % i):
#             return False
#     return True
#
# l = list(map(lambda x: is_primal(x), range(2, 12)))
# print(l)
# print(any(l), all(l))

# s1 = list(range(10))
# s2 = "hello ali!"
# x1 = zip(s1, s2)
# x2 = enumerate(s2)
# x = list(x1)
# y = list(x2)
# print(x == y)
# print(list(x1))
# print(y)

# s = '1 - hellow / n2 - 5 +'\
#     '3 hello'
# x = list(filter(lambda x: not x.isalpha(),s))
# print(x)
# x = list(reversed(x))
# print(x)
# x = [str(ord(c)) if c.isnumeric() else c for c in x if c != ' ']
# print(x)
# x = ''.join(x)
# print(x)
# x = eval(x)
# print(x)
# x = round(x, 3)
# print(x)
# x = hex(int(x*10))
# print(x)

# a_dict = {'a': 1, 'b': 2}
# a_l_of_tuple = [('a', 1), ('b', 2)]
# def tuple_dict_converter(data):
#     if isinstance(data, dict):
#         return list(map(lambda item: item, data.items()))
#     else:
#         return dict(map(lambda item: item ,data))
#
# print(tuple_dict_converter(a_l_of_tuple))

# from math import factorial
#
# # input n
# m = 0
# n = 5
# for i in range(n):
#     # for j in range(n - i + 1):
#     #     for left spacing
#         # print(end=" ")
#
#     for j in range(i + 1):
#         # nCr = n!/((n-r)!*r!)
#         print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
#
#     # for new line
#     print()
# print(id(n))
# print(id(m))
# a = ['1', ['2'], '3', '3']
# x = set(a)
# print(x)
# from hashlib import sha256
# print(sha256('1'.encode('utf-8')).hexdigest())
# print(sha256('2'.encode('utf-8')).hexdigest())
# print(sha256('3'.encode('utf-8')).hexdigest())
# print(sha256('3'.encode('utf-8')).hexdigest())
def palindrom(s):
    if s == s[::-1]:
        print('palindrome')
    else:
        print('not palindrome')


def show_employee(name, salary=9000):
    print(f'name: {name} salary: {salary}')


name = 'jafar'
salary = 25000
show_employee(name)