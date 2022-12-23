import re

text = 'fabdfb fsdbg'
pattern = r'\b.+a[b]*\w*\b'
result = re.findall(pattern, text)
print(result)

