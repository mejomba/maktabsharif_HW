import re

text = 'salamb'
pattern = r'^.*a.*b$'
result = re.findall(pattern, text)
print(result)

