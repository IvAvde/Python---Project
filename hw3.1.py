def div(a, b):
    if b != 0:
        divided = a / b
        print(divided)
    else:
        print('не дели на ноль!')
div(int(input('введите а - ')), int(input('введите b - ')))
