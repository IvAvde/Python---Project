def info(name=0, surname=0, yob=0, city=0, email=0, phone=0):
    name = input('введите имя - ')
    surname = input('введите фамилию - ')
    yob = input('введите год рождения - ')
    city = input('введите название города - ')
    email = input('введите имейл - ')
    phone = input('введите номер телефона - ')
    print('Ваши данные - ', name, surname, yob, city, email, phone)
info()