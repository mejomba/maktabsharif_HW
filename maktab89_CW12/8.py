def fibonacci(n):
    if n in {0, 1}:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(6))
