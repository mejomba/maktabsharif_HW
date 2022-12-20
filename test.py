lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
copy = lst.copy()

boolian = False
for item in copy:
    boolian = not boolian
    if boolian:
        lst.remove(item)
del copy

print(lst)

print(None < 1)