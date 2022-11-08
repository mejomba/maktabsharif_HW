my_dict = {
    'key1': 'value1',
    'key2': 'value2'
}


new_dict = dict(map(lambda key: (my_dict[key], key), my_dict.keys()))
print(new_dict)

# new_dict = {}
# for k,v in my_dict.items():
#     new_dict[v] = k
# print(new_dict)