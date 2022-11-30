# f = c * (9/5) + 32
def celsius_to_fahrenheit(c):
    return c * (9/5) + 32

data = [12, 24, 18, 40, 31]
out = list(map(celsius_to_fahrenheit, data))
print(out)
