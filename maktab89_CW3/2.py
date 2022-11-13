data = {'T-shirt':45.5, 'Pants':35, 'Sneakers':41.30, 'Hat':55, 'Backpack': 24}
def top3(d):
    sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))
    dic = dict()
    for i in range(3):
        a, b = sorted_dict.popitem()
        dic[a] = b
    return dic

print(top3(data))