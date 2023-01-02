import re


text = 'fgdfb z fszdg dsfb@'
pattern = r'\b\w*z\w*\b'
result = re.findall(pattern, text)
print(result)
