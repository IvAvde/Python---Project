basic_list = [1, 30, 4, 3, 58, 95, 85, 7, 19]
new_list = []
for num, el in enumerate(basic_list):
    if basic_list[num] > basic_list[num-1]:
        new_list.append(basic_list[num])
        print(num, el)
