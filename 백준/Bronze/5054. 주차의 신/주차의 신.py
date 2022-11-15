t = int(input())
for _ in range(t):
    a = int(input())
    l = list(map(int, input().split()))
    d = 0
    l.sort(reverse=True)
    for i in range(a - 1):
        d += l[i] - l[i + 1]
    print(d * 2)
