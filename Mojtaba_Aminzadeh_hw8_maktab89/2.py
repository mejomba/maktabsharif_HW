import re


text = 'The FirstProgrammingBootcamp'

pattern = r'[^\s]([A-Z])'

for search in re.finditer(pattern, text):
    text = re.sub(pattern=pattern, repl=f'{search.group(0)[0]} {search.group(1)}', string=text, count=1)
print(text)
