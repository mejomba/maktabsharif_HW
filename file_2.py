

# numbers = map(int, input().split(','))
numbers = [int(x) for x in input().split(' ')]
print(numbers)
e = 0
o = 0

for i in numbers:
    if i % 2 == 0:
        e += 1
    else:
        o += 1
print(f"odd: {o}  even: {e}")

