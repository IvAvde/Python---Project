from sys import argv
from itertools import cycle
blist = [ 1, 5, 'f', 'e', 8, 45, 'k']
c = 0
sname, a = argv
a = int(a)
for el in cycle(blist):
    if c > a:
        break
    else:
        print(el)
    c += 1
