def add(a, b):
    if a < 0 and b < 0 or a>0 and b>0:
        if a == 0:
            return a
        elif a == 1:
            return b
        else:
            return abs(b) + add(abs(a)-1, abs(b))

    elif a < 0:
        return -(b + add(abs(a) - 1, b))
    else:
        return -(abs(b) + add(a - 1, abs(b)))


print(add(10, -2))

#
def add2(a, b):
    if b == 0:
        return 0
    elif b < 0:
        return - (a - add2(a, b + 1))
    else:
        return a + add2(a, b - 1)

print(add2(10, -2))