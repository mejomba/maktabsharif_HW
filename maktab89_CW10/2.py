import re

text = 'dfsgsbdf'
pattern = r'.a+[b]*'
result = re.findall(pattern, text, flags=re.I)
print(result)

