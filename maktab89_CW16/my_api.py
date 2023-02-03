import requests
from pprint import pprint


output = {}

api_key = 'UZB0NiBUuYTaO7WTLOR68A==UGF3GmAIB6p420Rt'

for i in range(1, 10):
    word = input(f'get word {i}: ')
    params = {'word':word}
    headers = {'X-Api-Key': api_key}
    url = f'https://api.api-ninjas.com/v1/dictionary'
    res = requests.get(url, headers=headers, params=params)
    if res.status_code == requests.codes.okay:
        data = res.json()
        output[data['word']] = data['definition']
    else:
        print('request error')
pprint(output)