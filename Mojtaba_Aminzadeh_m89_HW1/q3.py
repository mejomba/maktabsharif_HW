# =================== HW 1 ===================
# =================== q3 ===================
""" author: Mojtaba Aminzadeh """

data = [1, 2, 2, 'sds4', 3, 3, 'sds4', 5]
out = [*set(data)] # first (don't support unhashable type)
# out = [*dict.fromkeys(data)] # second (don't support unhashable type)
# out = list(set(data)) # third (don't support unhashable type)
# out = list(dict.fromkeys(data)) # forth (don't support unhashable type)

# fifth (support unhashable type)
# out = []
# for d in data:
#     if d not in out:
#         out.append(d)

print(out)
