li_st = input('-')
li_st = list(li_st)
first_el = 0
sec_el = 0
a = 0
b = 1
c = int(li_st[-1])
new_list = []
while first_el < len(li_st) and sec_el < len(li_st) and a <= len(li_st) and b <= len(li_st):
    if sec_el < len(li_st) - 1:
        first_el = int(li_st[a])
        sec_el = int(li_st[b])
        new_list.append(sec_el)
        new_list.append(first_el)
        a += 2
        b += 2
    else:
        new_list.append(c)
        break
print(new_list)
