# =================== HW 1 ===================
# =================== q1 ===================
vowels = 'aeoiu'
user_input = input()
user_input = user_input.replace(' ', '') # remove all spaces

# swap lower and upper
# temp = ""
# for c in user_input:
#     if c.isupper():
#         temp += c.lower()
#     elif c.islower():
#         temp += c.upper()
# user_input = temp

user_input = user_input.swapcase() # simple way for swap lower and upper :)

for ch in vowels: # replace vowel words with "."
    if ch in user_input.lower():
        user_input = user_input.replace(ch.lower(), '.').replace(ch.upper(), '.')

print(user_input)
# Mohammad Amin Tehrani >>> m.H.MM.D.M.Nt.HR.N.
# =================== q2 ===================
for row in range(1, 6):
    for col in range((5-row)+1, 0, -1):
        print(col, end=" ")
    print()

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# =================== q3 ===================
data = [1,2,2,'sds4',3,3,'sds4',5]
out = [*set(data)] # first (can't compare unhashable type)
# out = [*dict.fromkeys(data)] # second (can't compare unhashable type)
# out = list(set(data)) # third (can't compare unhashable type)
# out = list(dict.fromkeys(data)) # forth (can't compare unhashable type)

# fifth (can compare unhashable type)
# out = []
# for d in data:
#     if d not in out:
#         out.append(d)

print(out)

# =================== q4 ===================
user_input = int(input())
print(user_input[::-1]) # firs way

# second way
# out = [*str(user_input)][::-1]
# print(*out, sep='')

# third way
# result = 0
# while user_input > 0:
#     result += (user_input % 10) * 10** (len(str(user_input)) -1)
#     user_input = user_input // 10
# print(result)

# =================== q5 ===================
# admin admin >>> Welcome on Admin
# admin wrongpass >>>“Wrong”
# jafar akbar >>> Hello jafar”
username, password = input().split()
user_check = username == 'admin'
pass_check = password == 'admin'
if user_check and pass_check:
    print('Welcome on Admin')
elif user_check and not pass_check:
    print("Wrong")
else:
    print(f'Hello {username}')

# =================== q6 ===================
user_input = int(input())
divisor_list = []
for number in range(1, user_input):
    if user_input % number == 0:
        divisor_list.append(number)
out = "YES" if sum(divisor_list) == user_input else "NO"
print(out)
