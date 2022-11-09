# =================== HW 1 ===================
# =================== q1 ===================
""" author: Mojtaba Aminzadeh """

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
