stroka = input('пиши:')
spisok = stroka.split( )
for num, el in enumerate(spisok):
    el = str(el)
    if len(el) <= 10:
        print(num, el)
    else:
        el = list(el)
        el = el[0] + el[1] + el[2] + el[3] + el[4] + el[5] + el[6] + el[7] + el[8] + el[9]
        print(num, el)