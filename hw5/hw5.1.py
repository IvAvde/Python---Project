with open('hw5.1.txt', 'w', encoding='utf-8') as f:
    while True:
        st = input('введите текст')
        f.write(f'{st}\n')
        if not st:
            break
