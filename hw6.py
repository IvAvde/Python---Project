start = float(input('начальный результат:'))
end = float(input('цель:'))
day_count = 0
while start < end:
    start = 1.1*start
    day_count += 1
print(day_count)