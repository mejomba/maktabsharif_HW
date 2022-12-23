import re


text = 'The quick brown fox jumps over the lazy dog.'
pattern = r'fox'
result = re.search(pattern, text)

print(result)
print(result.span())
print(result.start())
print(result.end())
print(result.group())
