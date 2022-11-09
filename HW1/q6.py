# =================== HW 1 ===================
# =================== q6 ===================
""" author: Mojtaba Aminzadeh """

user_input = int(input())
divisor_list = []
for number in range(1, user_input):
    if user_input % number == 0:
        divisor_list.append(number)
out = "YES" if sum(divisor_list) == user_input else "NO"
print(out)