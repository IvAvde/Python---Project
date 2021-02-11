blist = [5, 79 , 989 ,87, 36, 85, 4, 76, 5, 79, 989, 36]
nlist = [blist[1]]
for el in blist:
    if el in nlist:
        nlist.remove(el)
    else:
        nlist.append(el)



print(nlist)
