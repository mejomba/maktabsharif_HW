import re


text = 'abc2 abc abc3 abc123efg'
pattern = r'\b\w+\d\b'
result = re.findall(pattern, text)
print(result)
