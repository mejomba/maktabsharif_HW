data = [(2, 5),(1, 2),(4, 4),(2, 3),(2, 1)]
if all(data):
    out = sorted(data, key=lambda x: x[-1])
    print(out)
