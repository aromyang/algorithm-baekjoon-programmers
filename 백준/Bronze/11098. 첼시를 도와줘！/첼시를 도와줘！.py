n = int(input())
for _ in range(n):
    p = int(input())
    d = {}
    for _ in range(p):
        a, b = input().split()
        d[int(a)] = b
    print(d.get(max(d.keys())))
