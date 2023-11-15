p1 = [4, -5]
p2 = [2, 3, -6]

res = [0]*(len(p1) + len(p2) - 1)
for ix1,item1 in enumerate(p1):
    for ix2,item2 in enumerate(p2):
        res[ix1 + ix2] += item1*item2


print(res)