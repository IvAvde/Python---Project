number = input('введи число')
number = int(number)
last_digit = 0
largest_digit = 0
while number > 0:
    last_digit = number % 10
    if last_digit > largest_digit:
        largest_digit = last_digit
    number = number//10
print(largest_digit)