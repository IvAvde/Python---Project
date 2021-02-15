from functools import reduce
blist = list(range(100, 1001))
def reduction(prel, el):
    return prel * el
print(reduce(reduction, blist))