def sequence_avg():
    n = 0
    summa = 0
    flag = True
    a = 0
    while flag:
        a = int(input())
        if a == 0:
            flag = False
        summa += a
        n += 1
    if (n-1) > 0:
        print(round(float(summa/(n-1)), 2))
    else:
        print(0)


sequence_avg()
