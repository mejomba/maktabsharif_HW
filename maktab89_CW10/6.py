import re

text = 'fgdfb dfdbb fsdg dsfdsbbb'
pattern = r'\b[^b^\s]+b{2,3}\b'
result = re.findall(pattern, text)
print(result)

