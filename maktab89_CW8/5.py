import re

text = 'fgdfabbb fsdg dsfdsbbb'
pattern = r'\b.*ab{3}\b'
result = re.findall(pattern, text)
print(result)

