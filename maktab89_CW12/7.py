def check_prime(n, div=None):
    if not div:
        div = n - 1

    while div >= 2:
        if n % div == 0:
            return False
        else:
            return check_prime(n, div - 1)
    else:
        return True

print(check_prime(13))