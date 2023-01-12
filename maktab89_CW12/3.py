def pow_(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base

    if exp > 0:
        return base * pow_(base, exp - 1)


print(pow_(2, 2))