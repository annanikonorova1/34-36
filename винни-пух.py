def stih(str):
    str=str.split()
    list_a=[]
    for slovo in str:
        sum_s=0
        for i in slovo:
            if i in "аюиоеёыэуя":
                sum_s+=1
        list_a.append(sum_s)
    return len(list_a) == list_a.count(list_a[0])


str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if stih(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')