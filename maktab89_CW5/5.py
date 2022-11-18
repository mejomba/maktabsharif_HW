import random

data = set()
while len(data) != 3:
    x = random.randrange(100, 999, 5)
    # if x % 5 == 0:
    data.add(x)

print(data)
