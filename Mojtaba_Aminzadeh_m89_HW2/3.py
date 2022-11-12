def is_prime(number):
    if number > 1:
        for n in range(2, int(number ** 0.5) + 1):
            if number % n == 0:
                return False
        return True
    return 'number must be greater than 1'

print(is_prime(12))
print(is_prime(7))