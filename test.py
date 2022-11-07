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

