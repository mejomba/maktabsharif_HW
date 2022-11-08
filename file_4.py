# 'abc', 'xyz'
# out = 'xyc abz'
# inp1, inp2 = input().split()
inp1, inp2 = 'abc', 'xyz'

x = inp1.replace(inp1[:2], inp2[:2])
y = inp2.replace(inp2[:2], inp1[:2])
out = x + " " + y
print(out)

