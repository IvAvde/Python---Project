blist = list(range(20, 240))
nlist = []
for el in blist:
    if el % 20 == 0 or el % 21 == 0:
        nlist.append(el)
print(nlist)