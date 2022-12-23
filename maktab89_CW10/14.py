import re


text = 'fgdzfb z5A @ab_c fsgz dsfb@'
pattern = r'\w+'
result = re.findall(pattern, text)
print(result)

