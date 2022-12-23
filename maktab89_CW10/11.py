import re

punc = """!()-[]{};:'"\,<>./?@#$%^&*_~'"""

text = 'fgdfb fsdg dsfb?'
pattern = r'\w+[\?\!\)\@]$'
result = re.findall(pattern, text)
print(result)

