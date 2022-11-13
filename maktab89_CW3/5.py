data = {}
def ADD(k, v):
    if k not in data.keys():
        data[k] = v
        print('با موفقیت اضافه شد')
    else:
        print(f'کلید {k} موجود است')
        return True


def REMOVE(k, v):
    if k in data.keys() and v == data.get(k):
        data.pop(k)
        print('با موفقیت حذف شد')
    else:
        print('مقدار ارسالی اشتباه است')


while len(data) != 1:
    d = input('> ').split(' ')
    if not (ADD(d[0], d[1])):
        print(data)

while True:
    key, value, operator = input('> ').split(' ')
    if operator == 'add':
        ADD(key, value)
    elif operator == 'remove':
        REMOVE(key, value)
    else: break
    print(data)

print(data)

