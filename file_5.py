passwd = input().split(',')
print(passwd)
symb = ['@', '#', '$']
l_alpha = []
u_alpha = []
for i in range(97, 123):
    l_alpha.append(chr(i))
    u_alpha.append(chr(i).upper())
for pas in passwd:
    if 6<=len(pas)<=12:
        for ch in pas:
            if ch in symb and i in l_alpha and:
                pass