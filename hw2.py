seconds = int(input('введи время в секундах'))
hours = seconds//3600
minutes1 = seconds%3600
minutes = minutes1//60
seconds1 = seconds-(3600*hours)-(60*minutes)

print(hours,':', minutes,':', seconds1)