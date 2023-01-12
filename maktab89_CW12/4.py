def print_rec(n):
    if n >= 0:
        print(n)
        return print_rec(n -1)
    # elif n < 0:
    #     print(n)
    #     return print_rec(n + 1)
    # else:
    #     print(0)


print_rec(5)