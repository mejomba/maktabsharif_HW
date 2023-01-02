import re

text = 'fgdfb dfdbb fsdg dsfdsbbb'
pattern = r'^\w+'
result = re.findall(pattern, text)
print(result)

