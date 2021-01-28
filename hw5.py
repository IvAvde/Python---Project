income = input('выручка:')
liability = input('издержки:')
income = int(income)
liability = int(liability)
if income > liability:
    print('Вы в плюсе')
elif income == liability:
    print('вышли в ноль')
else:
    print('работай лучше')