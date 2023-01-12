lst = [1,3,4,5]


def iterator(iterable):
    if len(iterable) > 0:
        print(iterable[0])
        # yield iterable[0]
        return iterator(iterable[1:])
    # yield iterable[0]
    # print(iterable[0])

# print(list(iterator(lst)))
iterator(lst)





# a = {7: ({...}, 7)}
