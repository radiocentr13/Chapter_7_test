def tribonacci(k):
    a = []
    if k == 0:
        print(2)
        return
    i = 3
    a.extend([0, 0, 1])
    while True:
        a.extend([a[i-1]+a[i-2]+a[i-3]])
        if a[i] > k:
            break
        i += 1
    print(i)

k = int(input())
tribonacci(k)