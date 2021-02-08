def int_func():
    stroka = input('Введите текст')
    stroka = list(stroka.split())
    count = 0
    while count < len(stroka):
        slovo = str(stroka[count])
        count += 1
        print(slovo.title())
int_func()