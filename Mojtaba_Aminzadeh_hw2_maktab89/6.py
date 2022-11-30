from string import printable
from collections import Counter



data = '''Www.google.com'''


out = {}

for ch in printable:
    if ch in data:
        out[ch] = data.count(ch)

print(out)
