import re


text = '5fgdzfb z fszdgz dsfb@'
number = 6
pattern = r'\b^{number}.*\b'
result = re.findall(pattern, text, flags=re.I)
print(result)

res = re.compile(pattern)
print(res.pattern)