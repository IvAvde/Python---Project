from math import factorial
n = 20
def generator():
    for el in (range(1, n+1)):
        yield factorial(el)

g = generator()

for el in g:
    print(el)