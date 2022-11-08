inp = input().split(' ')
# inp = ['abc', 'xyz', 'aba', '1221']
counter = 0

for ch in inp:
    if len(ch) >= 2 and ch[0] == ch[-1]:
        print(ch)
        counter += 1
print(counter)
