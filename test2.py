data = [1, 2, 3, 4]


def iterator(iterable):
    if len(iterable) > 0:
        yield iterable[0]
        yield from iterator(iterable[1:])


print(list(iterator(data)))
for item in iterator(data):
    print(item)


# a = {7: (dict(), 7)}
# print(a[7][0])

x = dict().setdefault(7, 'default')
print(x[7])
