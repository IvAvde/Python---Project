income = int(input('выручка:'))
liability = int(input('издержки:'))
gain = 0
proporion = 0
per_wo = 0
if income > liability:
    gain = income - liability
    proporion = income / liability
    print('Вы в плюсе на', gain, 'в', proporion, 'раз окупились вложения')
    workers = int(input('Сколько работников потребовалось?'))
    per_wo = gain / workers
    print('Каждый работник заработал для компании', per_wo)

elif income == liability:
    print('вышли в ноль')
else:
    print('работай лучше')