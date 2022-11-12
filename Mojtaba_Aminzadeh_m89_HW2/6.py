from string import printable

data = 'www.google.com'
out = {}

for ch in printable:
    if ch in data:
        out[ch] = data.count(ch)

print(out)
