t = int(input())
for _ in range(t):
    n = int(input())
    a = 0
    b = 0
    for _ in range(n):
        c, g = map(float, input().split())
        a += c
        b += (c * g)
    print(int(a), round(b / a, 1))
