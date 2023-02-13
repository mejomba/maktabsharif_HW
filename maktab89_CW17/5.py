from bs4 import BeautifulSoup
from pprint import pprint


dictionary = {}
url = 'index.html'
res = open('index.html', 'r')

soup = BeautifulSoup(res.read(), 'html.parser')
result = soup.find_all('h2')

for i, item in enumerate(result, 1):
    dictionary[i] = item.text

pprint(dictionary)
