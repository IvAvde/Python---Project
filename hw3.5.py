summ = 0
def calculate():
    global summ
    count = 0
    enterednumbers = input('введите числа через пробел - ')
    enterednumbers = enterednumbers.split()
    if enterednumbers[-1] == 'E':
        if len(enterednumbers) == 1:
            print('Процесс окончен')
        else:
            while count < (len(enterednumbers) - 1):
                a = int(enterednumbers[count])
                summ += a
                count += 1
            print(summ, 'Процесс окончен')

    else:
        while count < len(enterednumbers):
            a = int(enterednumbers[count])
            summ += a
            count += 1
        print(summ)
        calculate()

calculate()
