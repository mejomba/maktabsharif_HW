# =================== HW 1 ===================
# =================== q5 ===================
""" author: Mojtaba Aminzadeh """

username, password = input().split()
user_check = username == 'admin'
pass_check = password == 'admin'
if user_check and pass_check:
    print('Welcome on Admin')
elif user_check and not pass_check:
    print("Wrong")
else:
    print(f'Hello {username}')

# admin admin >>> Welcome on Admin
# admin wrong-pass >>> “Wrong”
# jafar akbari >>> Hello jafar”