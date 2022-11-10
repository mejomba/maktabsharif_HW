def is_power(x, y):
    while x != 1 and x > 1:
        x /= y
    return True if x == 1 else False


print(is_power(128, 2))
