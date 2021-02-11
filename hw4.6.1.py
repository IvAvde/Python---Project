from sys import argv
from itertools import count
script_name, start = argv
start = int(start)
for el in count(start):
    if el > 100:
        break
    else:
        print(el)