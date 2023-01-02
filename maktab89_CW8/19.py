import re


text = 'The quick brown fox jumps over the lazy dog.'
pattern1 = r'fox'
pattern2 = r'dog'
pattern3 = r'horse'
result1 = re.search(pattern1, text)
result2 = re.search(pattern2, text)
result3 = re.search(pattern3, text)
print(result1)
print(result2)
print(result3)
