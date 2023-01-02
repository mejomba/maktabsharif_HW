import re

text = 'dsfAA sdaF fdsfsdSDFDS'
pattern = r'\b[a-z]+[A-Z]{1}\b'
result = re.findall(pattern, text)
print(result)

