a = input('начальный результат:')
b = input('цель:')
a = float(a)
b = float(b)
day_count = 0
while a < b:
    a = 1.1*a
    day_count += 1
print(day_count)