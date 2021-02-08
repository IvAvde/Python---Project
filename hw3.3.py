def my_func(a, b, c):
    if a > c and b > c:
        print(a + b)
    elif b > a and c > a:
        print(b + c)
    else:
        print(a + c)
my_func(7, 60, 3)
