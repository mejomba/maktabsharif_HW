import re


# Iran (Persian: ایران Irān [ʔiːˈɾɒːn] (About this soundlisten)), also called Persia[11] and officially the
# Islamic Republic of Iran (Persian: ایران اسالمی جمهوری Jomhuri-ye Eslāmi-ye Irān (About this
# soundlisten) [dʒomhuːˌɾije eslɒːˌmije ʔiːˈɾɒn]), is a country in Western Asia.


def read_file():
    with open('iran.txt', 'r') as file:
        return file.read()


text = read_file()

pattern = r'\b[A-Z]\w+\b'
res = set(re.findall(pattern, text))
# res = set(res)

with open('result.txt', 'w') as file:
    print(*res, file=file, sep='\n')

"""
Iran
Persian
Irān
About
Persia
Islamic
Republic
Jomhuri
Eslāmi
Wester
Asia
"""