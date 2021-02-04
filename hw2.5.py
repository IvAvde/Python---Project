rating = [9, 6, 5, 2]
score = int(input('новый элемент?'))
count = -1
allowed = True
while count < len(rating):

    if rating[count] == score:
        rating.insert(count, score)
        count += 1

        print(rating)
        break


    else:
        count += 1