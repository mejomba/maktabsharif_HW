'''Get the index and the value as a tuple for items in the
list ["hi", 4, 8.99, 'apple', ('t,b','n')].
Result would look like [(index, value), (index, value)]'''

data = ["hi", 4, 8.99, 'apple', ('t,b','n')]
out = [(idx, value) for idx, value in enumerate(data)]

sentence = "on a summer day somner smith went simming in the sun and his red skin stung"
data = sentence.split(' ')

out1 = list(filter(lambda x: len(x)>= 4,data))
out2 = list(filter(lambda x: len(x)< 4,data))
print(out1)
print(out2)