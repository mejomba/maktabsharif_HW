from math import factorial

print(factorial(10))

def fact(x):
    if x == 1 :
        return 1
    else:
        return x * fact(x-1)

print(fact(10))