def name():
    return 'mojtaab'


def arange(n):
    while n > 0:
        yield n
        n -= 1

# for i in arange(3):
#     print(i)

# even = [x for x in range(10) if x % 2 == 0]
even = (x for x in range(10) if x % 2 == 0)
print(even)
for i in even:
    print(i)
print()
for j in even:
    print(j)
