with open('hw5.2.txt') as f:
    st_c = 0
    stroki = f.readlines()
    w_count = 0
    for s in stroki:
        st_c += 1
        w_in_s = s.split()
        w_count += len(w_in_s)
        print('line number:', st_c, '     number of words:', w_count)
        w_count  = 0
    print('total number of strings:', st_c)