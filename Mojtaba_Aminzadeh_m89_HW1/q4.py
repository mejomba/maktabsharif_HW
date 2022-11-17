# =================== HW 1 ===================
# =================== q4 ===================
""" author: Mojtaba Aminzadeh """

user_input = int(input())
print(int(str(user_input)[::-1])) # firs way

# second way
# out = [*str(user_input)][::-1]
# print(*out, sep='')

# third way
result = 0
while user_input > 0:
    result += (user_input % 10) * 10** (len(str(user_input)) -1)
    user_input = user_input // 10
print(result)
