import re


text = 'fgdzfb z fszdgz dsfb@'
pattern = r'\b[a-y]+z[a-y]+\b'
result = re.findall(pattern, text, flags=re.I)
print(result)

