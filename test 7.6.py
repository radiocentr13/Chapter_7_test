def gcd(a, b):
    if b == 0:
        print(a)
    else:
        gcd(b, a % b)

a = int(input())
b = int(input())
gcd(a, b)