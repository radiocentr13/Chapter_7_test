def triangle(a, b, c):
    if a == b == c and a > 0:
        print("acute")
        return
    if a <= 0 or b <= 0 or c <= 0:
        print("impossible")
        return
    if a == b:
        gypotenuza, katet_1, katet_2 = c, b, a
    if b == c:
        gypotenuza, katet_1, katet_2 = a, b, c
    if c == a:
        gypotenuza, katet_1, katet_2 = b, c, a
    if a > b and a > c:
        gypotenuza, katet_1, katet_2 = a, b, c
    if b > a and b > c:
        gypotenuza, katet_1, katet_2 = b, a, c
    if c > b and c > a:
        gypotenuza, katet_1, katet_2 = c, b, a
    if gypotenuza >= katet_1 + katet_2:
        print("impossible")
        return
    if gypotenuza ** 2 < (katet_1 ** 2 + katet_2 ** 2):
        print("acute")
    if gypotenuza ** 2 > (katet_1 ** 2 + katet_2 ** 2):
        print("obtuse")
    if gypotenuza ** 2 == (katet_1 ** 2 + katet_2 ** 2):
        print("right")


a, b, c = int(input()), int(input()), int(input())
triangle(a, b, c)