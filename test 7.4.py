def sequence_max_even():
    n = 0
    max = 0
    a = 0
    max = 0
    while True:
        a = int(input())
        if a == 0:
            break
        if a % 2 == 0 and a > max:
            max = a
        n += 1
    print(max)


sequence_max_even()