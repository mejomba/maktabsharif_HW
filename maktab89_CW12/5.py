def print_rec(n):

    if n != 0:
        print_rec(n - 1)
    print(n)


print_rec(-5)