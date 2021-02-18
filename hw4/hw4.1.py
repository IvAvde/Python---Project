from sys import argv
script_name, h_salary, hours = argv
h_salary = int(h_salary)
hours = int(hours)
from random import random
bonus = random()
bonus += 1
salary = h_salary*hours*bonus
print(salary)
