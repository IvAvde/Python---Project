with open('hw5.3.txt') as f:
    workers = {line.split()[0]: float(line.split()[1]) for line in f}
    print('Average = ', {sum(workers.values()) / len(workers)})
    print('low payed: ', {el[0] for el in workers.items() if el[1] < 20000})