def my_func(x, y):
    if x > 0 and y < 0:
        count = 0
        while count > y:
           x = x*x
           count -= 1
    print(1 / x)
my_func(2, -3)