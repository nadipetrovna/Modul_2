
#first_stoun = random.randint(3, 20)
#print(first_stoun)

first_stoun = int (input('Введите случайное чило от 3 до 20:'))
result = []
for i in range(1,10):
    for j in range(2, 20):
        if first_stoun % (i+j) == 0 and i < j:
            result.append(i)
            result.append(j)
            continue
        else:
            continue
print(*result)