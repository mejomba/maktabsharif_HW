import re


text = 'abc2 123 abc 45 abc3 abc1234efg'
pattern = r'\b(\d{1,3})\b'
result = re.findall(pattern, text)
print(result)
